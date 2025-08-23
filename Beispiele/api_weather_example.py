import requests

def get_coordinates(city):
    """
    Nutzt die Open-Meteo Geocoding API, um
    den Städtenamen in Koordinaten (lat, lon) umzuwandeln.
    """
    print("Suche Koordinaten für Stadt:", city)
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1, "language": "de", "format": "json"}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "results" in data:
            result = data["results"][0]
            return result["latitude"], result["longitude"]
        else:
            print("Keine Ergebnisse für Stadt:", city)
            return None, None
    else:
        print("Fehler beim Abrufen der Koordinaten")
        return None, None


def get_weather_by_city(city):
    """
    Holt Wetterdaten nur anhand des Stadtnamens.
    """
    latitude, longitude = get_coordinates(city)
    if latitude is None or longitude is None:
        return

    print("Suche Wetterdaten für Koordinaten:", latitude, longitude)
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data.get("current_weather", {})
        print(f"Stadt: {city}")
        print(f"Aktuelle Temperatur: {weather.get('temperature')} °C")
        print(f"Aktuelle Windgeschwindigkeit: {weather.get('windspeed')} km/h")
    else:
        print("Fehler beim Abrufen der Wetterdaten")


# Beispiel
get_weather_by_city("Berlin")