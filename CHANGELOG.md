# Changelog

## 2026-06-16 — Codebase Cleanup

### Added
- `requirements.txt` (matplotlib, numpy, xlwt)
- `.gitignore` (venv, __pycache__, .vscode, .DS_Store, output data)
- `README.md` with setup and architecture overview
- `CLAUDE.md` with project conventions
- `CHANGELOG.md`

### Changed
- **BREAKING:** `variable.disease_status` → `variable.DiseaseStatus` (PEP 8 enum naming)
- `src/Shape.py` → `src/shape.py` (snake_case consistency)
- `good data/` → `good_data/` (no spaces in directory names)
- `ui.py`: wildcard tkinter imports → explicit `import tkinter as tk`
- `excel.py`: eager workbook init → lazy init pattern
- `ppmodel.py`: module-level side effects → `init_popular_places()` function
- `main.py`: bare `main()` call → `if __name__ == "__main__"` guard
- All files: tabs → 4-space indentation, docstrings added
- `mobility_model.py`: removed unused `import person`, fixed None init

### Removed
- `venv/` from git tracking (20,966 files)
- `.vscode/settings.json` from git tracking
- Dead imports: `from time import sleep`, `from numpy import average`
- Dead functions: `excel.start()`, `Shape.change_canvas()`
- Commented-out code blocks in `ppmodel.py`, `simulation.py`, `sir.py`
- `src/__pycache__/` from git tracking (previous commit)
