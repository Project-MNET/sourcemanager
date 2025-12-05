#!/usr/bin/env bash

echo "Running tests"

# Make sure src/ is in PYTHONPATH for imports
export PYTHONPATH=$(pwd)/src

# Start Flask in background
poetry run python src/index.py &
FLASK_PID=$!

echo "started Flask server"

# Wait until Flask is ready (default port 5000 used by src/index.py)
FLASK_PORT=5001
TIMEOUT=15
COUNT=0

while ! nc -z localhost $FLASK_PORT; do
    sleep 1
    COUNT=$((COUNT+1))
    if [ $COUNT -ge $TIMEOUT ]; then
        echo "Flask did not start within $TIMEOUT seconds"
        kill $FLASK_PID || true
        exit 1
    fi
done

echo "Flask server is ready"

# Run Robot Framework tests in story_tests
poetry run robot --variable HEADLESS:true src/story_tests

# Capture exit status
status=$?

# Kill Flask server
kill $FLASK_PID || true

# Exit with test status
exit $status
