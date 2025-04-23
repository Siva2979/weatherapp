from flask import Flask, render_template, request, flash
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for flashing messages
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
API_BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        try:
            params = {
                'q': city,
                'appid': WEATHER_API_KEY,
                'units': 'metric'
            }
            response = requests.get(API_BASE_URL, params=params)
            
            # Print debug information
            print(f"API URL: {response.url}")
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
            
            if response.status_code == 200:
                weather_data = response.json()
            else:
                error_data = response.json()
                flash(f"Error: {error_data.get('message', 'City not found')}", 'error')
        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}")
            flash("Error connecting to weather service. Please try again.", 'error')
        except Exception as e:
            print(f"Unexpected error: {e}")
            flash("An unexpected error occurred. Please try again.", 'error')
            
    return render_template('index.html', weather=weather_data, now=datetime.now())

if __name__ == '__main__':
    if not WEATHER_API_KEY:
        raise ValueError("No Weather API key set in .env file")
    app.run(host='0.0.0.0', port=5000, debug=True)