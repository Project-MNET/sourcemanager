echo "Running tests"

export FLASK_APP=src.app
export FLASK_RUN_PORT=5001
poetry run flask run &

FLASK_PID=$!

echo "started Flask server"

while [[ "$(curl -s -o /dev/null -w '%{http_code}' localhost:5001)" != "200" ]];
  do sleep 1;
done

echo "Flask server is ready"

poetry run robot --variable HEADLESS:true src/tests

status=$?

kill $(lsof -t -i:5001)

exit $status