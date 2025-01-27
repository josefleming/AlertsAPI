import requests

# API endpoint
url = 'https://511on.ca/api/v2/get/alerts'

# Fetch data
response = requests.get(url)
alerts = response.json()

import geojson

# Function to convert alerts to GeoJSON features
def alerts_to_geojson(alerts):
    features = []
    for alert in alerts:
        # Ensure the alert has latitude and longitude
        if 'latitude' in alert and 'longitude' in alert:
            point = geojson.Point((alert['longitude'], alert['latitude']))
            properties = {key: alert[key] for key in alert if key not in ['latitude', 'longitude']}
            features.append(geojson.Feature(geometry=point, properties=properties))
    return geojson.FeatureCollection(features)

# Convert alerts to GeoJSON
geojson_data = alerts_to_geojson(alerts)

# Save to a file
with open('alerts.geojson', 'w') as f:
    geojson.dump(geojson_data, f)


