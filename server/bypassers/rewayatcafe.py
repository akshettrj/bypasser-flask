import time
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def rewayatcafe_bypass(url):
    client = requests.Session()
    res = client.get(url)
    p = urlparse(url)
    ref = f'{p.scheme}://{p.netloc}/'

    h = {'referer': ref}

    res = client.get(url, headers=h)
    bs4 = BeautifulSoup(res.content, 'html.parser')
    inputs = bs4.find_all('input')
    data = { input.get('name'): input.get('value') for input in inputs }

    h = {
        'content-type': 'application/x-www-form-urlencoded',
        'x-requested-with': 'XMLHttpRequest'
    }
    p = urlparse(url)
    final_url = f'{p.scheme}://{p.netloc}/links/go'

    time.sleep(10)  # important
    res = client.post(final_url, data=data,  headers=h).json()
    try:
        return res['url']
    except Exception:
        return "Something went wrong :/"
