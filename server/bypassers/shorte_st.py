import re
import time
import requests
from urllib.parse import urlparse

# 404: Exception handling not found :(

def sh_st_bypass(url):
    client = requests.Session()
    client.headers.update({'referer': url})
    p = urlparse(url)

    res = client.get(url)

    sess_id = re.findall('''sessionId(?:\s+)?:(?:\s+)?['|"](.*?)['|"]''', res.text)[0]

    final_url = f"{p.scheme}://{p.netloc}/shortest-url/end-adsession"
    params = {
        'adSessionId': sess_id,
        'callback': '_'
    }
    time.sleep(5) # !important

    res = client.get(final_url, params=params)
    dest_url = re.findall('"(.*?)"', res.text)[1].replace('\/','/')

    return dest_url
