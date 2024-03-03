from flask import Flask, jsonify
import json
import os

app = Flask(__name__)


@app.route("/get_data", methods=["GET"])
def get_data():
    # Check if the JSON file exists
    if os.path.exists("fake_data.json"):
        # Open and read the JSON file for each request
        with open("fake_data.json", "r") as file:
            data = json.load(file)
        return jsonify(data)
    else:
        return jsonify({"error": "Data not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
