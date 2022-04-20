import requests
from base64 import b64decode


def sirigan_bypass(url):
    client = requests.Session()
    res = client.get(url)
    url = res.url.split('=', maxsplit=1)[-1]

    while True:
        try:
            url = b64decode(url).decode('utf-8')
        except Exception:
            break

    return url.split('url=')[-1]
