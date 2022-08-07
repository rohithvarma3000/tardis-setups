import requests
import os


def download_from_url(url):
    try:
        print("Started http")
        r = requests.get(url)
        print("Request complete")
        if r.status_code % 100 == 4:
            raise Exception("File not found or url not authorised")
        if r.status_code % 100 == 5:
            raise Exception("Unable to download file due to server error")

        fname = r.headers.get("Content-Disposit").split("filename=")[1]
    except AttributeError:
        fname = url.split("/")[-1].split("?")[0]

    file_path = os.path.join(os.path.expanduser("~"), "Downloads", "tardis-data", fname)
    try:
        open(file_path, "x")
    except FileNotFoundError:
        pass
    open(file_path, "wb").write(r.content)

    return file_path
