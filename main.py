import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env (if available)
load_dotenv()

# Create a Flask app
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing)
# Allow requests from any origin and only allow GET requests
CORS(app, resources={r"/products": {"origins": "*"}}, methods=["GET"])

# Define a route for "/products"
@app.route("/products", methods=["GET"])
def get_products():
    # Return a JSON list of product objects
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]
    return jsonify(products)

if __name__ == "__main__":
    # Fetch the port from environment variables or default to 3030
    port = int(os.getenv("PORT", 3030))
    # Run the Flask server on 0.0.0.0 (accessible externally) and chosen port
    app.run(host="0.0.0.0", port=port)
