from flask import Flask, jsonify, request
import requests
import os 

app = Flask(__name__)

BACKEND_URL = os.environ.get("BACKEND_URL")
    
@app.route('/api', methods=['GET'])
def get_data():
    try:
        # Send a GET request to the backend service
        response = requests.get(BACKEND_URL)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response from the backend service
            data = response.json()
            # Return the data as JSON
            return jsonify(data)
        else:
            # Return an error message if the request was unsuccessful
            return jsonify({"error": "Failed to fetch data from the backend"}), 500
    except Exception as e:
        # Return an error message if an exception occurred
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'}), 200

@app.route('/api', methods=['POST'])
def send_data():
    try:
        user = request.args.get('user')
        age = request.args.get('age')
        data = {
            "user": user,
            "age": age
        }
        # Send a POST request to the backend service with the data
        print("THIS IS A TEST PRINT")
        print(user)
        print(age)
        response = requests.post(BACKEND_URL, json=data)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response from the backend service
            data = response.json()
            # Return the data as JSON
            return jsonify(data)
        else:
            # Return an error message if the request was unsuccessful
            return jsonify({"error": "Failed to send data to the backend"}), 500
    except Exception as e:
        # Return an error message if an exception occurred
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
