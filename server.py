#!/usr/bin/env python


# from lib import hello_world

from flask import Flask, render_template, request

app = Flask(__name__)

STEPS = {
    "select": "Select Date and Line/Station",
    "timetable": "Timetable",
}


@app.route("/")
def index():
    return render_template("index.html", steps=STEPS)


@app.route("/step/select")
def select():
    gtfs_url = request.args.get("gtfs_url")
    return render_template("select.html", gtfs_url=gtfs_url)


@app.route("/step/timetable")
def timetable():
    return render_template("timetable.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# hello_world()
