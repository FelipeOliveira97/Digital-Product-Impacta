from flask import Flask
import requests
import json
import os


app = Flask(__name__)

REQUEST_URL = os.environ.get("REQUEST_URL")

@app.route("/")
def all():
    request = requests.get(REQUEST_URL)
    data = json.loads(request.content)
    return data


@app.route("/status/<int:status_id>", methods=["GET"])
def status(status_id):
    request = requests.get(REQUEST_URL)
    data = json.loads(request.content)
    data = [x for x in data if x['codigo'] == status_id]
    return data

if __name__ == '__main__':
    app.run()

