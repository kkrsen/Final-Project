#!/usr/bin/env python


#from lib import hello_world

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    moutains = ["Everest", "K2", "Kilimanjaro"]
    return render_template("index.html", mountain = moutains)

@app.route("/mountain/<mt>")
def mountain(mt):
    return "This is " + str(mt)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)




#hello_world()

