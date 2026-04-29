# BREAK_GLASS_20260429_BICAMERAL_IMPORT_DEPENDENCY.md

## Constitutional Judgment Record

**Date:** 2026-04-29
**Trigger:** I4 — Traceability Is Mandatory
**Filed by:** Initial repo bootstrap
**Status:** NOTED — no action required, documented for transparency

---

## The Conflict

`bicameral_review.py` imports from `contract_window.py` using a relative import:

```python
from contract_window import ContractWindow, EvidenceBasis
```

This import will fail if both files are not on the Python path together. In the current directory layout (`governance-kernel/bicameral-review/` and `governance-kernel/contract-window/`), a naive `python bicameral_review.py` will raise `ModuleNotFoundError`.

---

## The Tension

**I4 (Traceability):** The dependency between modules should be explicit and traceable.
**I5 (Safety Over Fluency):** The correct architectural choice is to make the import work properly, not to collapse both files into one for convenience.
**I6 (Fail Closed):** Do not silently allow an import that will fail in standard use.

---

## Resolution

The correct resolution is to add a `governance-kernel/__init__.py` and a package structure, or to provide a `run_tests.sh` / `pytest.ini` that sets PYTHONPATH correctly. This is a first-week engineering task.

The files are written correctly for the research prototype stage. The import dependency is documented here rather than silently broken.

When the package structure is formalized, update this file to RESOLVED.

---

## Action Required

[ ] Add `governance-kernel/__init__.py` and package structure
[ ] Add `pytest.ini` or `pyproject.toml` with correct source root
[ ] Update this file to RESOLVED when complete

---

V&T: BREAK_GLASS_20260429_BICAMERAL_IMPORT_DEPENDENCY.md — EXISTS (written)
  → VERIFIED AGAINST: actual file paths in repo structure
  → NOT CLAIMED: resolution (this is an open action item)
  → FUNCTIONAL STATUS: constitutional judgment record, open
