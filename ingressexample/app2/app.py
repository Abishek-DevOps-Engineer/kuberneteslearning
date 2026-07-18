from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url, timeout=8)
    response.raise_for_status()
    data = response.json()

    current = data.get("current_condition", [{}])[0]
    area = data.get("nearest_area", [{}])[0]

    return {
        "city": area.get("areaName", [{}])[0].get("value", city),
        "country": area.get("country", [{}])[0].get("value", "Unknown"),
        "temperature_c": current.get("temp_C", "N/A"),
        "feels_like_c": current.get("FeelsLikeC", "N/A"),
        "humidity": current.get("humidity", "N/A"),
        "wind_kmph": current.get("windspeedKmph", "N/A"),
        "description": current.get("weatherDesc", [{}])[0].get("value", "No description"),
    }


@app.route("/weather", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    city = ""

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if not city:
            error = "Please enter a city name."
        else:
            try:
                weather = get_weather(city)
            except requests.RequestException:
                error = "Could not fetch weather data right now."
            except (IndexError, KeyError, ValueError):
                error = "Weather data was not available for that location."

    return render_template("index.html", weather=weather, error=error, city=city)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
