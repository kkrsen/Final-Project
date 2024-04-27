#!/usr/bin/env python


# from lib import hello_world

from flask import Flask, render_template

app = Flask(__name__)

STEPS = {
        "url_upload": "URL Upload",
        "select": "Select Date and Line/Station",
        "timetable": "Timetable",
    }

@app.route("/")
def index():
    return render_template("index.html", steps=STEPS)


@app.route("/step/url_upload")
def url_upload():
    return "This is where you upload your GTFS URL"

@app.route("/step/select")
def select():
    return "This is Select Date and Line/Station"

@app.route("/step/timetable")
def timetable():
    return "This is Timetable"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# hello_world()
