import requests
import geojson

def fetch_alerts():
    url = 'https://511on.ca/api/v2/get/alerts'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

def alerts_to_geojson(alerts):
    features = []
    for alert in alerts:
        # Replace 'Latitude' and 'Longitude' with the correct field names
        if 'Latitude' in alert and 'Longitude' in alert:
            try:
                latitude = float(alert['Latitude'])
                longitude = float(alert['Longitude'])
                point = geojson.Point((longitude, latitude))
                properties = {key: alert[key] for key in alert if key not in ['Latitude', 'Longitude']}
                features.append(geojson.Feature(geometry=point, properties=properties))
            except ValueError:
                print(f"Invalid coordinates for alert ID {alert.get('Id')}.")
        else:
            print(f"Alert ID {alert.get('Id')} is missing location data.")
    return geojson.FeatureCollection(features)

def main():
    alerts = fetch_alerts()
    if alerts:
        geojson_data = alerts_to_geojson(alerts)
        with open('alerts.geojson', 'w') as f:
            geojson.dump(geojson_data, f)
        print("GeoJSON data has been written to alerts.geojson.")
    else:
        print("No alerts to process.")

if __name__ == '__main__':
    main()
