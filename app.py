from flask import Flask, jsonify 

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Your Flask app is running successfully."

@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {"message": "This is a sample API response", "status": "success"}
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(debug=True)
