# Build step for the pin-allocation model. Source of truth = pins.yaml (+ solver/board.yaml).
# Generated Markdown views live in generated/ — never hand-edit those.
UV := /opt/homebrew/bin/uv
VENV := .venv
PY := $(VENV)/bin/python

.PHONY: all check render solve venv clean

all: check render solve

check: venv           ## cross-check the YAMLs (SoM-ball uniqueness, ranges, cross-file, sound conn)
	$(PY) check.py

venv: $(VENV)/.stamp
$(VENV)/.stamp: requirements.txt
	$(UV) venv $(VENV)
	VIRTUAL_ENV=$(VENV) $(UV) pip install -q -r requirements.txt
	touch $@

render: venv          ## regenerate generated/*.md from pins.yaml
	$(PY) render.py

solve: venv           ## run the CP-SAT validator (feasibility + Pareto + ledger)
	$(PY) solver/solve.py

clean:
	rm -rf $(VENV) generated solver/ledger.json solver/.venv
