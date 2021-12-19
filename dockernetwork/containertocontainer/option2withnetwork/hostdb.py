import psycopg2
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.get("/")
def landing_page():
    return "Welcome to Docker host connection with network request page"

@app.get("/details")
def get_details():
    try:
        #establishing the connection
        conn = psycopg2.connect(
        database="dockerdb", user='dockeruser', password='dockerpass', host=os.environ.get('POSTGRES_SERVICE_NAME'), port= '5432'
        )
        return "Connection to database is successful"
    except:
        return "Connection to database is failed"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9091)
