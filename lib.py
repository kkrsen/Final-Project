from gtfs_kit.feed import read_feed


def download_gtfs_file(url: str):
    feed = read_feed(url, dist_units="mi")
    stop_id = feed.stops["stop_id"]
    # filter out North/South duplicates
    stops = feed.stops[~stop_id.str.endswith("N")][~stop_id.str.endswith("S")].to_dict(
        orient="records"
    )
    stop_times = feed.stop_times.to_dict(orient="records")
    trips = feed.trips.to_dict(orient="records")
    routes = feed.routes.to_dict(orient="records")
    return stops, stop_times, trips, routes
