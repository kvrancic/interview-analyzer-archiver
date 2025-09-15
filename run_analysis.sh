#!/bin/bash
# Simple script to run the interview analysis

# Activate virtual environment
source venv/bin/activate

# Run with proper Python path
PYTHONPATH=. python src/main.py "$@"