#!/usr/bin/env python


from flask import Flask, render_template, request
import pandas as pd

from lib import download_gtfs_file

from gtfs_kit.feed import read_feed


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
    (
        stops,
        stop_times,
        trips,
        routes,
    ) = download_gtfs_file(gtfs_url)
    return render_template("select.html", gtfs_url=gtfs_url, stops=stops, routes=routes)


@app.route("/step/timetable")
def timetable():
    stop_id = request.args.get("stop")
    route_id = request.args.get("route")
    gtfs_url = request.args.get("gtfs_url")
    feed = read_feed(gtfs_url, dist_units="mi")
    if route_id is not None:
        timetable = feed.build_route_timetable(route_id=route_id, dates=["20240428"])
        timetable = list(timetable.groupby(by="stop_id"))
        stops = feed.stops.to_dict(orient="records")
        stop_timetables = []
        for stop_id, stop_timetable in timetable:
            stop_name = ""
            for stop in stops:
                if stop["stop_id"] == stop_id:
                    stop_name = stop["stop_name"]
                    break
            stop_timetable = stop_timetable.to_dict(orient="records")
            stop_timetables.append((stop_id, stop_name, stop_timetable))
            print(stop_timetable)
        return render_template(
            "timetable.html",
            stop_id=stop_id,
            route_id=route_id,
            stop_timetables=stop_timetables,
        )


if __name__ == "__main__":
    pd.options.display.max_columns = None
    app.run(host="0.0.0.0", port=5000)
