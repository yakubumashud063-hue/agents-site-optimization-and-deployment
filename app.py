from flask import Flask, render_template, request, redirect, url_for, abort, session, jsonify
from jinja2 import TemplateNotFound
from functools import wraps
from werkzeug.utils import secure_filename
import json
import time
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'farmfresh_secret_key_2025')

users_file = Path(__file__).parent / 'users.json'
products_file = Path(__file__).parent / 'products.json'
messages_file = Path(__file__).parent / 'messages.json'
orders_file = Path(__file__).parent / 'orders.json'
uploads_dir = Path(__file__).parent / 'static' / 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

if not uploads_dir.exists():
    uploads_dir.mkdir(parents=True, exist_ok=True)

# User storage helpers

def load_users():
    if users_file.exists():
        return json.loads(users_file.read_text())
    return {}


def save_users(users):
    users_file.write_text(json.dumps(users, indent=2))

# Product storage helpers

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def infer_category_from_filename(filename):
    lower = filename.lower()
    fruits = ['apple', 'banana', 'mango', 'orange', 'lemon', 'lime', 'pear', 'peach', 'grape', 'melon', 'watermelon', 'berry', 'strawberry', 'raspberry', 'blueberry', 'kiwi', 'pawpaw', 'pineapple', 'papaya', 'avocado', 'durian', 'mango', 'cherry']
    vegetables = ['tomato', 'carrot', 'potato', 'broccoli', 'cabbage', 'cucumber', 'okra', 'pepper', 'onion', 'garlic', 'spinach', 'lettuce', 'kale', 'parsley', 'ginger', 'pea', 'corn', 'beet', 'eggplant', 'cabbage', 'celery', 'ginger', 'yam']
    dairy = ['egg', 'milk', 'cheese', 'butter', 'yogurt']
    livestock = ['cow', 'goat', 'sheep', 'fowl', 'hen', 'chicken', 'rabbit', 'goats', 'sheep', 'fowls', 'guinea']
    meats = ['beef', 'pork', 'lamb', 'goat', 'chicken', 'mutton']

    if any(word in lower for word in fruits):
        return 'Fruits'
    if any(word in lower for word in vegetables):
        return 'Vegetables'
    if any(word in lower for word in dairy):
        return 'Dairy'
    if any(word in lower for word in livestock):
        return 'Livestock'
    if any(word in lower for word in meats):
        return 'Meats'
    return 'Other'
