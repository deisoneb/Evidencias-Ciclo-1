# src/python/server.py
from flask import Flask, request, jsonify
import json
from datetime import datetime
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ensure a directory exists for storing drawings
DRAWINGS_DIR = 'drawings'
os.makedirs(DRAWINGS_DIR, exist_ok=True)

@app.route('/')
def home():
    return jsonify(message="Servidor Python corriendo ")

@app.route('/save_drawing', methods=['POST'])
def save_drawing():
    data = request.json
    
    if not data or 'drawing' not in data:
        return jsonify({"error": "No se proporcionaron datos de dibujo"}), 400

    # Generate a unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"dibujo_{timestamp}.json"
    
    # Full path to save the file
    file_path = os.path.join(DRAWINGS_DIR, filename)
    
    # Save the drawing data to a JSON file
    with open(file_path, 'w') as f:
        json.dump(data, f)
    
    return jsonify({
        "message": "Dibujo guardado exitosamente!",
        "filename": filename
    }), 200

if __name__ == '__main__':
    app.run(debug=True)