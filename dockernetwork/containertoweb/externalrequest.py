import requests
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.get("/")
def landing_page():
    return "Welcome to Docker external network request page"

@app.get("/details")
def get_details():
    external_api_url = "http://jsonplaceholder.typicode.com/posts/1"
    external_response = requests.get(external_api_url)
    return jsonify(external_response.json())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9091)
