# Project Instructions

## Tech Stack
- **Language:** Python 3.9+
- **GUI:** Tkinter (built-in)
- **Visualization:** matplotlib + numpy
- **Data export:** xlwt (Excel)

## Code Style
- Classes: PascalCase (`Person`, `Location`, `PopularPlacesModel`)
- Enums: PascalCase (`DiseaseStatus.VULNERABLE`)
- Files: snake_case (`simulation.py`, `person.py`, `shape.py`)
- Methods/functions: snake_case (`try_infect`, `sim_main`)
- Constants: UPPER_SNAKE_CASE in `variable.py`
- Indentation: 4 spaces
- Docstrings: triple-quote style on all public functions
- Imports: stdlib first, blank line, third-party, blank line, local modules
- Entry point: `if __name__ == "__main__"` guard required

## Testing
- No test framework configured
- No test files exist

## Build & Run
- Install: `pip install -r requirements.txt`
- Run: `python src/main.py`
- Lint: `python -m py_compile src/*.py`

## Project Structure
```
src/
  main.py            → Entry point with __name__ guard
  simulation.py      → Main simulation loop (hour-by-hour iteration)
  person.py          → Person agent with disease states and infection logic
  variable.py        → All tunable simulation parameters
  location.py        → 2D coordinate with movement and distance helpers
  ppmodel.py         → Popular Places mobility model (home ↔ popular places)
  mobility_model.py  → Base mobility model class
  sir.py             → SIR epidemic model and matplotlib graphing
  ui.py              → Tkinter canvas UI (tk.Tk, not wildcard imports)
  shape.py           → Canvas drawing primitives (oval, square)
  excel.py           → xlwt Excel export with lazy init
Image/               → Screenshots and label images
data/                → Output data (gitignored)
good_data/           → Curated result images
```

## Architecture
Agent-based simulation. Main loop (`simulation.py::sim_main`) iterates hourly over all `Person` objects. Each person updates location via mobility model, progresses disease state, and tries to infect vulnerable neighbors within proximity. After simulation ends, SIR model is computed and plotted.

**Disease state machine:** VULNERABLE → INCUBATION → ASYMPTOMATIC or SYMPTOMATIC → IMMUNE or DEAD

**Infection logic:** Ordered fallback checks — home infection → masked+vaccinated → masked → vaccinated → normal. First matching probability check wins.

## Conventions
- Commit messages: simple lowercase one-liners
- Branch: `main` only, no feature branches
- No CI/CD
- Use module-level constants in `variable.py` for all tunable parameters
- Run `ppmodel.init_popular_places()` before using popular places
- Lazy-init pattern used in `excel.py` to avoid import-time side effects
