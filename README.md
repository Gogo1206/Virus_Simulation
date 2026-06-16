# Virus Simulation

Agent-based virus spread simulation with real-time Tkinter visualization. Models disease transmission through a population using SIR (Susceptible-Infected-Recovered) dynamics with masks, vaccines, social distancing, and popular-places mobility.

## Requirements

- Python 3.9+
- matplotlib
- numpy
- xlwt

## Setup

```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Run

```bash
python src/main.py
```

## How It Works

Each person is an agent with a disease state (vulnerable → incubation → asymptomatic/symptomatic → immune/dead) and a mobility model. People move between their home and popular places. Infection spreads by proximity. Masks, vaccines, and social distancing reduce transmission probability. After the simulation, an SIR model is computed and plotted alongside the simulation data.

## Parameters

All tunable parameters are in `src/variable.py`:
- Population size, simulation hours, initial infections
- Infection probabilities (normal, masked, vaccinated, home)
- Disease durations (incubation, symptomatic, asymptomatic)
- Mobility model settings (speed, stay time, distancing)

## Project Structure

```
src/                → All source code
  main.py           → Entry point
  simulation.py     → Main simulation loop
  person.py         → Person agent with disease states
  variable.py       → Tunable simulation parameters
  location.py       → 2D coordinate and movement helpers
  ppmodel.py        → Popular Places mobility model
  mobility_model.py → Base mobility model class
  sir.py            → SIR epidemic model and graphing
  ui.py             → Tkinter canvas visualization
  shape.py          → Canvas drawing primitives
  excel.py          → xlwt Excel data export
data/               → Output data
Image/              → Screenshots
good_data/          → Curated result images
```
