import requests

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        # Extract relevant weather information (e.g., temperature, description)
        return weather_data.get('main'), weather_data.get('weather')[0]
    else:
        return None

# Usage
api_key = "YOUR_API_KEY"
city = "New York"  # Replace with the desired city
weather = get_weather(api_key, city)
if weather:
    temperature = weather[0]['temp']
    description = weather[1]['description']
    print(f"The temperature in {city} is {temperature}°C with {description}.")
else:
    print("Failed to fetch weather data.")
