from flask import Flask
import requests
import json

app = Flask("Hello World")

@app.route("/status", methods=["GET"])
def status():
    request = requests.get("https://www.diretodostrens.com.br/api/status")
    data = json.loads(request.content)
    data = list(filter(lambda x: x['codigo'] == 1))
    return data
app.run()
