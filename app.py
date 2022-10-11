from flask import Flask
import requests
import json

app = Flask("Hello World")

@app.route("/status/{status_id}", methods=["GET"])
def status(status_id):
    request = requests.get("https://www.diretodostrens.com.br/api/status")
    data = json.loads(request.content)
    data = [x for x in data if x['codigo'] == status_id]
    return data
app.run()