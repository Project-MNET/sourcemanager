echo "Running tests"

poetry run python -m src.app &
FLASK_PID=$!

echo "started Flask server"

while ! nc -z localhost 5001; do
  sleep 1
done

echo "Flask server is ready"

poetry run robot --variable HEADLESS:true src/tests

status=$?

kill $FLASK_PID

exit $status