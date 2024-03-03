from flask import Flask, jsonify
import json

app = Flask(__name__)


# Endpoint to get the generated data
@app.route("/get_data", methods=["GET"])
def get_data():
    # Assuming the data is saved in a file named 'fake_data.json'
    try:
        with open("fake_data.json", "r") as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Data not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
