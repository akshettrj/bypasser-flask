import time
import cloudscraper
from bs4 import BeautifulSoup

def rocklinks_bypass(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    DOMAIN = "https://pastebin.techymedies.com"
    url = url[:-1] if url[-1] == '/' else url

    code = url.split("/")[-1]
    final_url = f"{DOMAIN}/{code}?quelle="

    resp = client.get(final_url)

    soup = BeautifulSoup(resp.content, "html.parser")
    inputs = soup.find(id="go-link").find_all(name="input")
    data = { input.get('name'): input.get('value') for input in inputs }

    h = { "x-requested-with": "XMLHttpRequest" }

    time.sleep(6)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    return r.json()['url']
