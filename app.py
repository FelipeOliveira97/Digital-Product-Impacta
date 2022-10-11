from flask import Flask

app = Flask(name)

@app.route("/status", methods=["GET"]")
def Status():
    return "Hello World"

if name == 'main':
    app.run()