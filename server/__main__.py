from . import app, BYPASSERS
from flask import request, jsonify
import json


@app.route('/api', methods=['POST'])
def json_api():

    data = request.data.strip()
    if len(data) == 0:
        return jsonify({"ok": False, "message": "No data provided"})

    try:
        data = json.loads(data)
    except json.JSONDecodeError as ex:
        return jsonify({"ok": False, "message": "Could not parse the data as JSON"})
    data_keys = data.keys()
    if (
        len(data_keys) != 2 or
        "type" not in data_keys or
        "url" not in data_keys
    ):
        return jsonify({"ok": False, "message": "Exactly two keys required: 'type' and 'url'"})

    bypasser_type, url_to_bypass = data['type'], data['url']
    if bypasser_type not in BYPASSERS.keys():
        return jsonify({"ok": False, "message": "Not a valid bypasser"})

    bypasser_func = BYPASSERS[bypasser_type]
    try:
        bypassed_link = bypasser_func(url_to_bypass)
    except Exception as ex:
        return jsonify({"ok": False, "message": f"Failed to bypass: {ex}"})

    return jsonify({"ok": True, "url": bypassed_link})


app.run(host='0.0.0.0', debug=True)
