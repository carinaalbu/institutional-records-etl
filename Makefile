# Makefile for Institutional Records Pipeline

# Python interpreter
PYTHON = python

# Directories
RAW_DIR = data/raw
PROCESSED_DIR = data/processed

.PHONY: all install run clean

# Default target: do everything
all: install run

# 1. Install dependencies using Conda
install:
	conda install --yes --file requirements.txt

# 2. Run the ETL pipeline
run:
	$(PYTHON) src/etl.py

# 3. Clean up processed data
clean:
	rm -rf $(PROCESSED_DIR)/*
	@echo "Cleaned processed data."