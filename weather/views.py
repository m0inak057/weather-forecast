import requests
import json
from django.shortcuts import render
from django.conf import settings
from datetime import datetime, timedelta # We'll need this for the history

def index(request):
    current_weather = {}
    daily_forecasts = []
    history_chart_data = None
    error_message = None

    if request.method == 'POST':
        city = request.POST.get('city', 'London')
        api_key = settings.OPENWEATHER_API_KEY
        
        # --- API URLs ---
        # 1. OpenWeatherMap (OWM) for Current Weather
        current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        try:
            # --- Call 1: Get Current Weather ---
            response = requests.get(current_weather_url).json()
            
            if response.get('cod') == 200:
                # Extract coordinates for the other API calls
                lat = response['coord']['lat']
                lon = response['coord']['lon']
                
                # Process current weather data
                current_weather = {
                    'city': response['name'],
                    'temperature': round(response['main']['temp']),
                    'description': response['weather'][0]['description'].title(),
                    'icon': response['weather'][0]['icon'],
                    'humidity': response['main']['humidity'],
                    'wind_speed': round(response['wind']['speed']),
                }
                
                # --- Call 2: OWM 5-Day Forecast ---
                forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric'
                forecast_response = requests.get(forecast_url).json()
                
                if forecast_response.get('cod') == '200':
                    full_forecast_list = forecast_response.get('list', [])
                    # Filter to get one forecast per day (at 12:00:00)
                    for item in full_forecast_list:
                        if "12:00:00" in item['dt_txt']:
                            daily_forecasts.append({
                                'day': datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S').strftime('%a'),
                                'temp': round(item['main']['temp']),
                                'icon': item['weather'][0]['icon'],
                            })
                
                # --- Call 3: Open-Meteo 30-Day History (No API Key needed!) ---
                today = datetime.now()
                # To be safe, let's set the end date 5 days ago, as the free API has a delay
                end_date_safe = today - timedelta(days=5)
                start_date = end_date_safe - timedelta(days=30)
                
                historical_url = (
                    f"https://archive-api.open-meteo.com/v1/archive?"
                    f"latitude={lat}&longitude={lon}"
                    f"&start_date={start_date.strftime('%Y-%m-%d')}"
                    f"&end_date={end_date_safe.strftime('%Y-%m-%d')}"
                    f"&daily=temperature_2m_max"
                )
                
                history_response = requests.get(historical_url).json()
                
                if history_response.get('daily'):
                    history = history_response['daily']
                    # Format for Chart.js
                    history_chart_data = json.dumps({
                        'labels': history['time'],
                        'data': history['temperature_2m_max'],
                    })
                elif history_response.get('error'):
                    # NEW: Catch errors from the history API
                    if error_message is None: # Only show if no other error
                        error_message = f"History Chart Error: {history_response.get('reason', 'Could not retrieve history.')}"

            else:
                error_message = f"Could not find weather data for '{city}'. Please try again."

        except requests.exceptions.RequestException:
            error_message = "Could not connect to the weather service. Please try again later."
        except Exception as e:
            error_message = f"An error occurred: {e}"

    context = {
        'current': current_weather,
        'forecasts': daily_forecasts,
        'history_chart_data': history_chart_data,
        'error_message': error_message
    }
    
    return render(request, 'weather/index.html', context)