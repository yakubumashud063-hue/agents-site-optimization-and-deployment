from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from jinja2 import TemplateNotFound

app = Flask(__name__)

# Temporary data storage
saved_items = []
messages = []
profiles = {
    "username": "JohnDoe",
    "email": "johndoe@example.com",
    "preferences": "Organic products only"
}

# Route for the homepage
@app.route('/')
def home():
    return render_template('template.html')

# Route for the Sell+ form submission
@app.route('/sell', methods=['POST'])
def sell():
    product_name = request.form.get('product-name')
    price = request.form.get('price')
    description = request.form.get('description')

    # Process or store the data (here we're just printing it)
    print(f"New item for sale: {product_name}, Price: {price}, Description: {description}")
    return redirect(url_for('home'))

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/fruits')
def fruits():
    return render_template('fruits.html')

@app.route('/vegetables')
def vegetables():
    return render_template('vegetables.html')

@app.route('/livestock')
def livestock():
    return render_template('livestock.html')

@app.route('/dairy')
def dairy():
    return render_template('dairy.html')

@app.route('/seeds_tools')
def seeds_tools():
    return render_template('seeds_tools.html')

@app.route('/meats')
def meats():
    return render_template('meats.html')

@app.route('/plus')
def plus():
    return render_template('plus+.html')

# Route for the Save section
@app.route('/save', methods=['POST'])
def save():
    item = request.json.get('item')
    saved_items.append(item)
    return jsonify({"message": "Item saved successfully!", "saved_items": saved_items})

# Route for the Messages section
@app.route('/messages', methods=['POST'])
def add_message():
    message = request.json.get('message')
    messages.append(message)
    return jsonify({"message": "Message added successfully!", "messages": messages})

# Route for the Profile section
@app.route('/profile')
def profile():
    return jsonify(profiles)


@app.route('/<page>.html')
def render_static_html(page):
    try:
        return render_template(f"{page}.html")
    except TemplateNotFound:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)