# web_app/routes/api_routes.py

from flask import Blueprint, request, jsonify

api_routes = Blueprint("api_routes", __name__)

@api_routes.route("/api/hello.json")
def hello():
    return jsonify({"message": "Hello World"}) # can jsonify a dictionary

@api_routes.route("/api/users.json")
def users():
    return jsonify([1,2,3]) # can jsonify a list

@api_routes.route("/api/forecast.json")
def forecast():
    print("URL PARAMS:", dict(request.args))
    zip_code = request.args["zip_code"] #> {'zip_code': '20057'}
    results = get_hourly_forecasts(zip_code)
    return jsonify(results)