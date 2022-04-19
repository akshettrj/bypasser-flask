# Flask Bypasser

Flask server that integrates various bypassing scripts with API support

## Usage

### Starting the Server

1. Install the required python packages: `pip install -r requirements.txt`
2. Start the server: `python3 -m server`
3. The server will start at port 5000 by default or if you have `PORT` environment variable set,
   it will use that port

### Making Requests

1. You can make `POST` requests to the server
2. The endpoint will be `/api`
3. The data should be in json format and should have two keys:
    1. `type` - Specifies which bypasser to use
    2. `url` - Specifies the link which to bypass
4. The returned json data has a field `ok` (boolean) specifying if some error occurred
5. In case of error, a field `message` is returned containing the error
6. Otherwise a key `url` contains the bypassed link

## Available Bypassers

* The following bypassers (with corresponding types) are supported:

| S.No. | Bypasser    | Type          |
|-------|-------------|---------------|
| 1.    | Adfly       | `adfly`       |
| 2.    | Droplink    | `droplink`    |
| 3.    | Gplink      | `gplinks`     |
| 4.    | Linkvertise | `linkvertise` |
| 5.    | Ouo         | `ouo`         |
| 6.    | Rocklinks   | `rocklinks`   |
| 7.    | Shorte      | `shorte`      |

---

* Thanks to [Yukki](https://github.com/xcscxr) for bypassing scripts
* Thanks to [Zek](https://github.com/ZekXtreme) for motivation
