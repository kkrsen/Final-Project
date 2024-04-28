from io import BytesIO
from zipfile import ZipFile
import requests
import pandas as pd
from gtfs_kit.feed import read_feed


def download_gtfs_file(url: str):
    feed = read_feed(url, dist_units="mi")
    df_stops = pd.DataFrame(feed.stops)
    df_stops = df_stops.groupby("stop_name").first().reset_index()
    stops = df_stops["stop_name"].tolist()
    print(stops)
    df_routes = pd.DataFrame(feed.routes)
    routes = df_routes["route_id"].tolist()
    print(routes)
