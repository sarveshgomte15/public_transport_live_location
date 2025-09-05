from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Store bus data temporarily
bus_data = {}

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    bus_id = data.get("bus_id")
    lat = data.get("lat")
    lon = data.get("lon")

    if bus_id and lat and lon:
        bus_data[bus_id] = {"lat": lat, "lon": lon}
        return jsonify({"status": "success", "message": f"Bus {bus_id} updated."})
    else:
        return jsonify({"status": "error", "message": "Missing data"}), 400

@app.route('/get_location/<bus_id>', methods=['GET'])
def get_location(bus_id):
    if bus_id in bus_data:
        return jsonify({"bus_id": bus_id, "location": bus_data[bus_id]})
    else:
        return jsonify({"status": "error", "message": "Bus not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
