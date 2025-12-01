import os
from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_time():
    tz_name = request.args.get("tz", "Europe/Kyiv")

    try:
        tz = pytz.timezone(tz_name)
    except Exception:
        return jsonify({"error": f"Unknown timezone '{tz_name}'"}), 400

    now = datetime.now(tz)

    return jsonify({
        "timezone": tz_name,
        "datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
        "day": now.strftime("%A"),
        "utc_offset": now.strftime("%z")
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
