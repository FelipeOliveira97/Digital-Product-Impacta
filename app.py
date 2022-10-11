from flask import Flask
import requests
import json

app = Flask("Hello World")

@app.route("/status", methods=["GET"])
def status():
    request = requests.get("https://www.diretodostrens.com.br/api/status")
    data = json.loads(request.content)
    data = [x for x in data if x['codigo'] == 1]
    return data
app.run()
