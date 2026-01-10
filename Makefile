# Pipeline Makefile

PYTHON = python

.PHONY: all install verify clean analyze

# The Full Workflow
all: install verify clean analyze

install:
	conda install --yes --file requirements.txt

# Step 1: Validate Integrity
verify:
	$(PYTHON) src/checksum.py verify

# Step 2: Clean Data (Depends on Verify passing)
clean: verify
	$(PYTHON) src/etl.py

# Step 3: Analyze & Report (Depends on Clean passing)
analyze: clean
	$(PYTHON) src/analyze.py

# Utility: Remove generated files
reset:
	rm -rf data/processed/*
	rm -rf reports/pipeline_summary.txt
	@echo "Pipeline reset."