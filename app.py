from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "poc"

@app.route("/cdn-images/stock/y/yf17vwj-7-l.jpg")
def hello():
    return "blabla"
