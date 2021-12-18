from flask import Flask, request, jsonify
import json

app = Flask(__name__)

file_location = "/app/countries.json"

def read_json_data():
    # Opening JSON file
    with open(file_location, 'r') as openfile:
        json_object = json.load(openfile)
        return json_object
  
def write_josn_data(in_json):
    with open(file_location, 'w') as f:
        json.dump(in_json, f)

# countries = [
#     {"id": 1, "name": "India", "capital": "Delhi", "area": 10003120},
#     {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
#     {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
# ]

countries = [
    {"id": 1, "name": "India", "capital": "Delhi", "area": 10003120}
]

write_josn_data(countries)

def _find_next_id(countries):
    """
    Return next in sequence country id
    """
    return max(country["id"] for country in countries) + 1

@app.get("/")
def landing_page():
    return "Welcome to simple flask api"


@app.get("/countries")
def get_countries():
    countries = read_json_data()
    return jsonify(countries)

@app.post("/countries")
def add_country():
    print("add_countryadd_countryadd_countryadd_countryadd_countryadd_countryadd_country")
    if request.is_json:
        country = request.get_json()
        countries = read_json_data()
        country["id"] = _find_next_id(countries)
        countries.append(country)
        write_josn_data(countries)
        return country, 201
    return {"error": "Request must be JSON"}, 415

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9090)


