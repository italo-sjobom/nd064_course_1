from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def statusResponse():
    return '{} ; {} ; {}'.format("Status Code: 200", "JSON: {'user': 'admin'}", "result: OK - healthy")

@app.route("/metrics")
def metricsResponse():
    return '{} ; {}'.format("JSON: {'user': 'admin'}", "data: {UserCount: 140, UserCountActive: 23}")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    app.run(port='5000')
