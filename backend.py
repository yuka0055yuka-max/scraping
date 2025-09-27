# backend.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from scraper_logic import perform_scrape

app = Flask(__name__, static_folder="static")
CORS(app)

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/manifest.json")
def manifest():
    return send_from_directory("static", "manifest.json")

@app.route("/service-worker.js")
def sw():
    return send_from_directory("static", "service-worker.js")

@app.route("/api/scrape", methods=["POST"])
def api_scrape():
    data = request.get_json()
    url = data.get("url")
    keywords = data.get("keywords", [])
    password = data.get("password", None)
    result = perform_scrape(url, keywords, password)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
