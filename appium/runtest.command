#!/bin/bash

echo "🚀 Starting Automation Run..."

# --------- CONFIG ---------
PROJECT_DIR="$(cd "$(dirname "$0")"; pwd)"
VENV_DIR="$PROJECT_DIR/.venv"
APPIUM_PORT=4723
LOG_FILE="$PROJECT_DIR/appium.log"

# --------- ACTIVATE VENV ---------
echo "🔹 Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# --------- START APPIUM SERVER ---------
echo "🔹 Starting Appium server..."
appium --port $APPIUM_PORT --log $LOG_FILE &
APPIUM_PID=$!

# Wait for Appium to fully start
sleep 10

# --------- RUN TESTS ---------
echo "🧪 Running test suite... :$PROJECT_DIR"
python3 -m unittest discover -s "$PROJECT_DIR" -p "runner.py"

TEST_EXIT_CODE=$?

# --------- STOP APPIUM ---------
echo "🛑 Stopping Appium server..."
kill $APPIUM_PID

# --------- RESULT ---------
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "✅ Tests Passed!"
else
    echo "❌ Tests Failed!"
fi

exit $TEST_EXIT_CODE
