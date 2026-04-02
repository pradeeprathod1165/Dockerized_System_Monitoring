from flask import Flask
import time
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Monitoring App Running!"

@app.route("/load")
def load():
    # simulate CPU load
    x = 0
    for i in range(10000000):
        x += i
    return "Load generated"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
