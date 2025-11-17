echo "Running tests"

poetry run python3 src/index.py &

echo "started Flask server"

while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5001)" != "200" ]];
  do sleep 1;
done

echo "Flask server is ready"

poetry run robot --variable HEADLESS:true src/tests

status=$?

kill $(lsof -t -i:5001)

exit $status