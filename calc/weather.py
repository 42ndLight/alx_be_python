import requests

# Define your API key and the endpoint URL
api_key = 'YOUR_API_KEY'  # Replace with your actual OpenWeather API key
lat = -1.2921  # Latitude for Nairobi
lon = 36.8219  # Longitude for Nairobi
exclude = ''  # Parts to exclude from the API response, e.g., 'minutely,hourly'

# Construct the API URL
url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={api_key}'

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    # Access specific weather information
    current_temp = data['current']['temp']
    weather_description = data['current']['weather'][0]['description']
    print(f"Current temperature: {current_temp}K")
    print(f"Weather description: {weather_description}")
else:
    print(f"Error: Unable to fetch data (Status code: {response.status_code})")
