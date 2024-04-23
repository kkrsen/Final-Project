from io import BytesIO
from zipfile import ZipFile
import requests


def hello_world():
    print("Hello World")

def download_gtfs_file(url: str):
    response = requests.get(url)
    zip = ZipFile(BytesIO(response.content))
    print(zip.filelist)
