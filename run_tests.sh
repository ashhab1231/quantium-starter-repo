#!/bin/bash

echo "Activating virtual environment..."

# Activate venv
source venv/Scripts/activate

echo "Running test suite..."

# Run pytest
python -m pytest -v --headless --webdriver Chrome
TEST_RESULT=$?

# Check result
if [ $TEST_RESULT -eq 0 ]; then
    echo "All tests passed ✅"
    exit 0
else
    echo "Tests failed ❌"
    exit 1
fi
