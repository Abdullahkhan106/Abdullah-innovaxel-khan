from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
import random, string
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Define the SQLite database path (saved in the current folder)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "database.db")

# Configure SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Database Model
class ShortURL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(2048), nullable=False)
    short_code = db.Column(db.String(6), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    access_count = db.Column(db.Integer, default=0)

# Function to Generate a Unique Short Code
def generate_shortcode():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Create Database (Run only once)
with app.app_context():
    db.create_all()

# 1. Create Short URL (POST)
@app.route('/shorten', methods=['POST'])
def create_short_url():
    data = request.get_json()
    if 'url' not in data:
        return jsonify({"error": "URL is required"}), 400

    shortcode = generate_shortcode()
    while ShortURL.query.filter_by(short_code=shortcode).first():
        shortcode = generate_shortcode()

    new_url = ShortURL(url=data['url'], short_code=shortcode)
    db.session.add(new_url)
    db.session.commit()

    return jsonify({
        "id": new_url.id,
        "url": new_url.url,
        "shortCode": new_url.short_code,
        "createdAt": new_url.created_at,
        "updatedAt": new_url.updated_at
    }), 201

# 2. Retrieve Original URL (GET)
@app.route('/shorten/<short_code>', methods=['GET'])
def get_original_url(short_code):
    short_url = ShortURL.query.filter_by(short_code=short_code).first()
    if not short_url:
        return jsonify({"error": "Short URL not found"}), 404

    short_url.access_count += 1
    db.session.commit()

    return jsonify({
        "id": short_url.id,
        "url": short_url.url,
        "shortCode": short_url.short_code,
        "createdAt": short_url.created_at,
        "updatedAt": short_url.updated_at
    }), 200

# 3. Update Short URL (PUT)
@app.route('/shorten/<short_code>', methods=['PUT'])
def update_short_url(short_code):
    short_url = ShortURL.query.filter_by(short_code=short_code).first()
    if not short_url:
        return jsonify({"error": "Short URL not found"}), 404

    data = request.get_json()
    if 'url' not in data:
        return jsonify({"error": "URL is required"}), 400

    short_url.url = data['url']
    db.session.commit()

    return jsonify({
        "id": short_url.id,
        "url": short_url.url,
        "shortCode": short_url.short_code,
        "createdAt": short_url.created_at,
        "updatedAt": short_url.updated_at
    }), 200

# 4. Delete Short URL (DELETE)
@app.route('/shorten/<short_code>', methods=['DELETE'])
def delete_short_url(short_code):
    short_url = ShortURL.query.filter_by(short_code=short_code).first()
    if not short_url:
        return jsonify({"error": "Short URL not found"}), 404

    db.session.delete(short_url)
    db.session.commit()

    return '', 204  # No Content

# 5. Get URL Statistics (GET)
@app.route('/shorten/<short_code>/stats', methods=['GET'])
def get_url_stats(short_code):
    short_url = ShortURL.query.filter_by(short_code=short_code).first()
    if not short_url:
        return jsonify({"error": "Short URL not found"}), 404

    return jsonify({
        "id": short_url.id,
        "url": short_url.url,
        "shortCode": short_url.short_code,
        "createdAt": short_url.created_at,
        "updatedAt": short_url.updated_at,
        "accessCount": short_url.access_count
    }), 200

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
