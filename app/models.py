from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    travel_date = db.Column(db.String(50), nullable=False)
    forecast = db.Column(db.String(100))  # Example: "Cloudy, 25°C"
    recommendation = db.Column(db.String(200)) # Example: "Bring a jacket!"