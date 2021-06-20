from flask import Flask
from flask import json
import logging
import time

app = Flask(__name__)

@app.route('/status')
def status():
    
    timestamp = time.time()
    endPointName = "status"
    logging.debug("%s, %s endpoint was reached", timestamp, endPointName)

    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json',
    )

    return response

@app.route('/metrics')
def metrics():
    
    timestamp = time.time()
    endPointName = "metrics"
    logging.debug("%s, %s endpoint was reached", timestamp, endPointName)

    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    return response

@app.route("/")
def hello():
    logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode="w", format='%(name)s - %(levelname)s - %(message)s')
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')