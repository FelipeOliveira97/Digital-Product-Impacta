from flask import Flask
import requests
import json


app = Flask(__name__)

@app.route("/", methods=["GET"])
def status():
    request = requests.get("https://www.diretodostrens.com.br/api/status")
    data = json.loads(request.content)
    return data


@app.route("/status/<int:status_id>", methods=["GET"])
def status(status_id):
    request = requests.get("https://www.diretodostrens.com.br/api/status")
    data = json.loads(request.content)
    data = [x for x in data if x['codigo'] == status_id]
    return data

if __name__ == '__main__':
    app.run()

