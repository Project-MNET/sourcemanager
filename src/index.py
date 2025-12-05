from app import app, initialize_database

if __name__ == "__main__":
    initialize_database()
    app.run(host="0.0.0.0", port=5001, debug=True)
