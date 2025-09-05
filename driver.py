import requests
import time
import random

URL = "http://127.0.0.1:5000/update_location"

lat = 18.5204
lon = 73.8567

while True:
    # add small random movement
    lat += random.uniform(-0.001, 0.001)
    lon += random.uniform(-0.001, 0.001)

    data = {
        "bus_id": "101",
        "lat": lat,
        "lon": lon
    }

    response = requests.post(URL, json=data)
    print("Updated:", response.json(), "Coords:", lat, lon)

    time.sleep(3)
