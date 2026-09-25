# Build step for the pin-allocation model. Source of truth = the module/board/product YAMLs
# (modules/, boards/, products/, common.yaml) assembled by model.py (+ solver/board.yaml).
# Generated Markdown views live in generated/<product>/ — never hand-edit those.
# Scope a single product with PRODUCT=<name>, e.g. `make check PRODUCT=bob`.
UV := /opt/homebrew/bin/uv
VENV := .venv
PY := $(VENV)/bin/python
PRODUCT ?=

.PHONY: all check render solve venv clean

all: check render solve

check: venv           ## cross-check every product (SoM-ball uniqueness, ranges, cross-file, KiCad)
	$(PY) check.py $(PRODUCT)

venv: $(VENV)/.stamp
$(VENV)/.stamp: requirements.txt
	$(UV) venv $(VENV)
	VIRTUAL_ENV=$(VENV) $(UV) pip install -q -r requirements.txt
	touch $@

render: venv          ## regenerate generated/<product>/*.md from the model
	$(PY) render.py

solve: venv           ## run the CP-SAT validator (feasibility + Pareto + ledger)
	$(PY) solver/solve.py

clean:
	rm -rf $(VENV) generated solver/ledger.json solver/.venv
