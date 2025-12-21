from app import create_app

# Create the application instance
app = create_app()

if __name__ == "__main__":
    # debug=True allows the server to restart automatically when you change code
    app.run(debug=True)