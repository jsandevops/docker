from flask import Flask, request, jsonify

app = Flask(__name__)

countries = [
    {"id": 1, "name": "India", "capital": "Delhi", "area": 10003120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    """
    Return next in sequence country id
    """
    return max(country["id"] for country in countries) + 1

@app.get("/")
def landing_page():
    return "Welcome to simple flask api"

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9090)


