# Simple flask homepage for discord server
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def homepage():
    message = "CatMafia Love's You!"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host='0.0.0.0')