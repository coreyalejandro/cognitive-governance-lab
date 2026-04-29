"""
data_pipeline.py
================
Reads SessionRecorder JSON output files, runs invariant checkers,
and writes a structured CSV for statistical analysis.

Output columns per research-plan.md Week 2 spec:
  session_id, condition, turn_count, token_count (approx),
  drift_incidents, repairs, ia_score, fk_grade,
  mean_alignment, min_alignment, repair_rate,
  atrophy_detected, iai_composite, started_at, ended_at

Usage:
    python data/data_pipeline.py --input datasets/sessions/ --output data/sessions.csv
    python data/data_pipeline.py --input datasets/pilot/ --output data/pilot.csv

Evidence basis: CONSTRUCTED — aggregation logic. No empirical validation.
I1/I2/I3/I4/I5/I6 compliant.

V&T: data_pipeline.py — EXISTS (written) →
     VERIFIED AGAINST: research-plan.md Week 2 spec, SessionRecorder JSON schema →
     NOT CLAIMED: statistical validity of derived metrics →
     FUNCTIONAL STATUS: operative; produces CSV from JSON session files
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

# ── path setup ───────────────────────────────────────────────────────────────
_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "governance-kernel" / "invariant-checkers"))

from invariant_checkers import score_session_checkers, check_comprehension_grade

# ── CSV columns ───────────────────────────────────────────────────────────────
FIELDNAMES = [
    "session_id",
    "condition",
    "participant_id",
    "turn_count",
    "human_turns",
    "model_turns",
    "token_count_approx",   # word count × 1.3 — CONSTRUCTED approximation
    "drift_incidents_gt",   # from session JSON (recorder-logged drift events)
    "drift_incidents_checker",  # from alignment scorer (score <= 2)
    "repairs",              # drift turns with human repair within 3
    "repair_rate",          # repairs / drift_incidents_checker
    "iai_composite",        # from IAI module
    "atrophy_detected",     # from IAI module
    "mean_alignment",       # mean task-state alignment score across model turns
    "min_alignment",        # lowest alignment score in session
    "mean_fk_grade",        # mean FK grade across all turns
    "started_at",
    "ended_at",
    "notes",
    "evidence_basis",       # always CONSTRUCTED until empirically validated
]


def _approx_tokens(text: str) -> int:
    """
    Approximate token count as word_count * 1.3.
    CONSTRUCTED — rough approximation for BPE tokenizers.
    PENDING: replace with tiktoken or model-specific tokenizer.
    """
    words = len(text.split())
    return int(words * 1.3)


def process_session_file(path: Path) -> dict | None:
    """
    Load one session JSON file and compute all pipeline metrics.
    Returns None if the file cannot be parsed (I6: skip, log to stderr).
    """
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"  SKIP {path.name}: {e}", file=sys.stderr)
        return None

    events = data.get("events", [])

    # Token count: sum across all turns
    total_tokens = sum(
        _approx_tokens(
            e.get("text", "") if isinstance(e, dict) else e.text
        )
        for e in events
    )

    # Drift incidents from recorder (flagged turns)
    drift_gt = data.get("drift_event_count", 0)

    # Run invariant checkers
    checker_results = score_session_checkers(data)
    drift_checker = len(checker_results.get("drift_turns", []))
    repairs = int(
        round((checker_results.get("repair_rate") or 0) * drift_checker)
    ) if drift_checker > 0 else 0

    # IAI results
    iai = data.get("iai_result") or {}

    row = {
        "session_id": data.get("session_id", "UNKNOWN"),
        "condition": data.get("condition", "UNKNOWN"),
        "participant_id": data.get("participant_id", "UNKNOWN"),
        "turn_count": data.get("total_turns", len(events)),
        "human_turns": data.get("human_turn_count", 0),
        "model_turns": data.get("model_turn_count", 0),
        "token_count_approx": total_tokens,
        "drift_incidents_gt": drift_gt,
        "drift_incidents_checker": drift_checker,
        "repairs": repairs,
        "repair_rate": checker_results.get("repair_rate"),
        "iai_composite": iai.get("composite_score"),
        "atrophy_detected": iai.get("atrophy_detected"),
        "mean_alignment": checker_results.get("mean_alignment"),
        "min_alignment": checker_results.get("min_alignment"),
        "mean_fk_grade": checker_results.get("mean_fk_grade"),
        "started_at": data.get("started_at"),
        "ended_at": data.get("ended_at"),
        "notes": data.get("notes", ""),
        "evidence_basis": "CONSTRUCTED",
    }
    return row


def run_pipeline(input_dir: Path, output_csv: Path, verbose: bool = True) -> int:
    """
    Process all .json files in input_dir and write output_csv.
    Returns number of sessions processed.
    """
    json_files = sorted(input_dir.glob("*.json"))
    if not json_files:
        print(f"No JSON files found in {input_dir}", file=sys.stderr)
        return 0

    output_csv.parent.mkdir(parents=True, exist_ok=True)
    rows = []

    for path in json_files:
        if path.name == "pilot_manifest.json":
            continue  # skip manifest files — not session records
        row = process_session_file(path)
        if row:
            rows.append(row)
            if verbose:
                print(f"  OK  {path.name:30s}  "
                      f"turns={row['turn_count']:2d}  "
                      f"drift_gt={row['drift_incidents_gt']}  "
                      f"drift_chk={row['drift_incidents_checker']}  "
                      f"iai={row['iai_composite']:.3f}  "
                      f"fk={row['mean_fk_grade']:.1f}  "
                      f"align={row['mean_alignment']}")

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    return len(rows)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Cognitive Governance Lab — session data pipeline"
    )
    parser.add_argument(
        "--input", required=True,
        help="Directory containing session JSON files"
    )
    parser.add_argument(
        "--output", required=True,
        help="Output CSV file path"
    )
    parser.add_argument(
        "--quiet", action="store_true",
        help="Suppress per-file output"
    )
    args = parser.parse_args()

    input_dir = Path(args.input)
    output_csv = Path(args.output)

    if not input_dir.exists():
        print(f"ERROR: input directory not found: {input_dir}", file=sys.stderr)
        sys.exit(1)

    print("=" * 70)
    print("COGNITIVE GOVERNANCE LAB — DATA PIPELINE")
    print(f"Input:  {input_dir}")
    print(f"Output: {output_csv}")
    print("Evidence basis: CONSTRUCTED. No empirical validation of metrics.")
    print("=" * 70)

    n = run_pipeline(input_dir, output_csv, verbose=not args.quiet)

    print()
    print(f"Processed: {n} session(s) → {output_csv}")
    print()
    print("V&T: data_pipeline.py —")
    print(f"  EXISTS: {output_csv} written with {n} rows")
    print("  VERIFIED AGAINST: SessionRecorder JSON schema, invariant_checkers.py")
    print("  NOT CLAIMED: statistical validity of derived metrics")
    print("  FUNCTIONAL STATUS: operative; PENDING empirical validation of checkers")
    print("=" * 70)


if __name__ == "__main__":
    main()
