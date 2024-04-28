#!/usr/bin/env python


from flask import Flask, render_template, request

from lib import download_gtfs_file

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
    stops, routes = download_gtfs_file(gtfs_url)
    return render_template("select.html", gtfs_url=gtfs_url, stops=stops, routes=routes)


@app.route("/step/timetable")
def timetable():
    stop_id = request.args.get("stop")
    route_id = request.args.get("route")
    route_color = request.args.get("route")
    return render_template(
        "timetable.html", stop_id=stop_id, route_id=route_id, route_color=route_color
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
