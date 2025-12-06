#!/usr/bin/env bash

echo "Running tests"

# Make sure src/ is in PYTHONPATH for imports
export PYTHONPATH=$(pwd)/src
# Make sure that coverage file is correct
export COVERAGE_FILE=$(pwd)/.coverage.robot

# Start Flask in background
poetry run coverage run --parallel-mode --source=src,src/database -m src.index &
#poetry run python src/index.py &
FLASK_PID=$!
trap "kill -TERM $FLASK_PID; wait $FLASK_PID || true" EXIT

echo "started Flask server (PID=$FLASK_PID)"

# Wait until Flask is ready (port 5001 used by src/index.py)
FLASK_PORT=5001
TIMEOUT=30
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
poetry run robot --variable HEADLESS:true --loglevel DEBUG src/story_tests

# Capture exit status
status=$?


#Nämä pitää kommentoida pois jotta github actions ei vahingossa käytä niitä turhaan.
#Niitä voi silti käyttää lokaalisti

#poetry run coverage combine
#poetry run coverage html

# Exit with test status
exit $status
