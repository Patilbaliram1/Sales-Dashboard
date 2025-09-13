<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Hello! Your Flask app is running successfully."

# Example API route
@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        "message": "This is a sample API response",
        "status": "success"
    }
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(debug=True)
=======
<<<<<<< HEAD
# app.py - placeholder Streamlit app
import streamlit as st

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Sales Dashboard - Placeholder")
st.write("This is a placeholder app. I'll replace this with the full dashboard code next.")
=======
# My Flask app 
>>>>>>> 0e6d476 (Add app.py file)
>>>>>>> f3576b0 (t push origin main)
