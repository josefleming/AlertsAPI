import requests
import json

url = "https://511on.ca/api/v2/get/alerts?format=json&lang=en"
response = requests.get(url)
data = response.json()

# Convert to GeoJSON format
geojson = {
    "type": "FeatureCollection",
    "features": []
}

for alert in data:
    feature = {
        "type": "Feature",
        "properties": {
            "Id": alert["Id"],
            "Message": alert["Message"],
            "Notes": alert["Notes"],
            "StartTime": alert["StartTime"],
            "EndTime": alert["EndTime"],
            "Regions": alert["Regions"],
            "HighImportance": alert["HighImportance"],
            "SendNotification": alert["SendNotification"]
        },
        "geometry": {
            "type": "Point",
            "coordinates": [0, 0]  # Placeholder coordinates
        }
    }
    geojson["features"].append(feature)

with open("alerts.geojson", "w") as f:
    json.dump(geojson, f)
