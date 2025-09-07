from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

buses = {}

@app.route("/update_location", methods=["POST"])
def update_location():
    data = request.json
    driver_id = data.get("driverId")
    if not driver_id:
        return jsonify({"error": "driverId required"}), 400

    buses[driver_id] = {
        "driver_id": driver_id,
        "bus_no": data.get("busNo"),
        "name": data.get("name"),
        "from": data.get("from"),
        "to": data.get("to"),
        "lat": data.get("lat"),
        "lng": data.get("lng"),
        "full": data.get("full"),
        "last_update": time.time()
    }
    return jsonify({"status": "ok"})

@app.route("/get_buses", methods=["GET"])
def get_buses():
    now = time.time()
    active_buses = [
        bus for bus in buses.values()
        if now - bus["last_update"] < 30
    ]
    return jsonify(active_buses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
