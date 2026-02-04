#!/bin/bash

# Move into the directory where the script lives
cd "$(dirname "$0")"
PROJECT_DIR=$(pwd)

echo "🚀 Starting Automation Run..."

# --------- CONFIG ---------
VENV_DIR="$PROJECT_DIR/.venv"
APPIUM_PORT=4723
LOG_FILE="$PROJECT_DIR/appium.log"

# --------- CLEANUP ---------
# Kill any old Appium sessions to avoid port conflicts
echo "🧹 Cleaning up old processes..."
kill -9 $(lsof -ti:$APPIUM_PORT) 2>/dev/null

# --------- ACTIVATE VENV ---------
echo "🔹 Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Ensure Python knows where your project folders are
export PYTHONPATH="$PROJECT_DIR"

# --------- START APPIUM SERVER ---------
echo "🔹 Starting Appium server..."
appium --port $APPIUM_PORT --log $LOG_FILE &
APPIUM_PID=$!

sleep 10 # Give Appium time to breathe

# --------- RUN TESTS ---------
echo "🧪 Running test suite via runner.py..."
python3 runner.py

TEST_EXIT_CODE=$?

# --------- STOP APPIUM ---------
echo "🛑 Stopping Appium server..."
kill $APPIUM_PID

# --------- RESULT ---------
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "✅ Tests Passed!"
else
    echo "❌ Tests Failed! Check appium.log for details."
fi

exit $TEST_EXIT_CODE