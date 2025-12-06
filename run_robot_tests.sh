#!/usr/bin/env bash

echo "Running tests"

# Make sure src/ is in PYTHONPATH for imports
export PYTHONPATH=$(pwd)/src

# Start Flask in background
poetry run coverage run --parallel-mode --source=src -m src.index &
#poetry run python src/index.py &
FLASK_PID=$!

echo "started Flask server"

# Wait until Flask is ready (port 5001 used by src/index.py)
FLASK_PORT=5001
TIMEOUT=15
COUNT=0
#On my machine this only works with ncat not nc. But in CI it only works on nc
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
kill -INT $FLASK_PID


wait $FLASK_PID

#Nämä pitää kommentoida pois jotta github actions ei vahingossa käytä niitä turhaan.
#Niitä voi silti käyttää lokaalisti

#poetry run coverage combine
#poetry run coverage html

# Exit with test status
exit $status
