# 🌍 Smart Travel Planner (Flask & REST API)

A dynamic web application that helps users plan their trips by providing real-time weather forecasts and automated packing recommendations based on live climate data.

## 🚀 Key Features
- **External API Integration:** Consumes the **OpenWeatherMap REST API** to fetch live weather data for any city worldwide.
- **Smart Recommendation Engine:** Implements custom logic to parse temperature and weather descriptions, providing tailored travel advice (e.g., "Pack light" vs "Bring a jacket").
- **Persistent Data Storage:** Uses **SQLAlchemy** to store trip history, including city names, dates, and specific recommendations.
- **Dynamic UI:** Built with **Jinja2 templates** and Bootstrap to display trip history in a clean, filterable table format.

## 🛠️ Tech Stack
- **Backend:** Python, Flask 
- **Database:** PostgreSQL / SQLite 
- **Libraries:** Requests (for API calls), Flask-SQLAlchemy, Dotenv 
- **Frontend:** HTML5, CSS3, Bootstrap 5 

## 💡 Engineering Highlights
- **Error Handling:** Implemented defensive programming to handle API status codes (e.g., 404 City Not Found or 401 Invalid Key).
- **Security:** Managed sensitive API credentials using **Environment Variables** (`.env`) to ensure secure deployment.
- **Application Factory Pattern:** Structured the project for scalability and easier testing.