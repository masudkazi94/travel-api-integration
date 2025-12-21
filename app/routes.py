import os
import requests
from flask import render_template, request, redirect, url_for, current_app as app
from .models import db, Trip

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        date = request.form.get('date')
        api_key = os.getenv('WEATHER_API_KEY')
        
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url)
            data = response.json()

            if data.get('cod') == 200:
                temp = data['main']['temp']
                weather_desc = data['weather'][0]['description']
                forecast_info = f"{weather_desc.capitalize()}, {temp}°C"

                # FIXED LOGIC FOR 17°C AND OTHERS
                if temp < 15:
                    advice = "It's cold! Bring a heavy jacket."
                elif 15 <= temp <= 22:
                    advice = "Mild weather. A light hoodie or jacket is best."
                elif temp > 22:
                    advice = "Warm weather! Pack light cotton clothes."
                
                # Rain check (overrides temperature advice if it's raining)
                if "rain" in weather_desc.lower():
                    advice += " Also, bring an umbrella!"

                new_trip = Trip(city=city, travel_date=date, forecast=forecast_info, recommendation=advice)
                db.session.add(new_trip)
                db.session.commit()
                return redirect(url_for('index'))
            else:
                return f"Error: {data.get('message')}", 400
        except Exception as e:
            return f"Error: {e}", 500

    trips = Trip.query.all()
    return render_template('index.html', trips=trips)

# NEW DELETE ROUTE
@app.route('/delete/<int:id>')
def delete_trip(id):
    trip_to_delete = Trip.query.get_or_404(id)
    db.session.delete(trip_to_delete)
    db.session.commit()
    return redirect(url_for('index'))