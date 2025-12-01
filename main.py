import functions_framework
from flask import request, jsonify
from datetime import datetime
import pytz

@functions_framework.http
def get_time(request):
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
