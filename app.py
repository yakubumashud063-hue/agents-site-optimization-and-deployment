from flask import Flask, render_template, request, redirect, url_for, abort, session, jsonify
from jinja2 import TemplateNotFound
from functools import wraps
import json
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'farmfresh_secret_key_2025'

# In-memory user database (for demo)
users_file = Path(__file__).parent / 'users.json'

def load_users():
    if users_file.exists():
        return json.loads(users_file.read_text())
    return {}

def save_users(users):
    users_file.write_text(json.dumps(users, indent=2))

def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Route for the homepage
@app.route('/')
def home():
    is_logged_in = 'username' in session
    return render_template('template.html', is_logged_in=is_logged_in, username=session.get('username'))

# User Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        
        if not username or not password:
            return render_template('register.html', error='Username and password required')
        
        users = load_users()
        if username in users:
            return render_template('register.html', error='Username already exists')
        
        users[username] = {'password': password, 'email': email}
        save_users(users)
        session['username'] = username
        return redirect(url_for('home'))
    
    is_logged_in = 'username' in session
    return render_template('register.html', is_logged_in=is_logged_in, username=session.get('username'))

# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        users = load_users()
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('home'))
        
        return render_template('login.html', error='Invalid credentials')
    
    is_logged_in = 'username' in session
    return render_template('login.html', is_logged_in=is_logged_in, username=session.get('username'))

# User Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

# Upload Product (requires login)
@app.route('/upload', methods=['POST'])
@require_login
def upload_product():
    product_name = request.form.get('product-name')
    price = request.form.get('product-price')
    description = request.form.get('product-description', '')
    
    if not product_name or not price:
        return jsonify({'error': 'Product name and price required'}), 400
    
    uploaded_by = session.get('username')
    product_data = {
        'name': product_name,
        'price': price,
        'description': description,
        'uploaded_by': uploaded_by
    }
    
    return jsonify({'success': True, 'message': f'Product "{product_name}" uploaded successfully!', 'product': product_data})

# Route for the Buy and Sell form submission
@app.route('/buy-sell', methods=['POST'])
def buy_sell():
    # Retrieve form data
    product_name = request.form.get('product-name')
    price = request.form.get('price')
    description = request.form.get('description')

    # Save the data (in this example, we're just printing it to the console)
    print(f"Product Name: {product_name}")
    print(f"Price: {price}")
    print(f"Description: {description}")

    # Redirect back to the homepage with a success message
    return redirect(url_for('home'))

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/fruits')
def fruits():
    is_logged_in = 'username' in session
    return render_template('fruits.html', is_logged_in=is_logged_in, username=session.get('username'))

@app.route('/vegetables')
def vegetables():
    is_logged_in = 'username' in session
    return render_template('vegetables.html', is_logged_in=is_logged_in, username=session.get('username'))

@app.route('/livestock')
def livestock():
    is_logged_in = 'username' in session
    return render_template('livestock.html', is_logged_in=is_logged_in, username=session.get('username'))

@app.route('/dairy')
def dairy():
    is_logged_in = 'username' in session
    return render_template('dairy.html', is_logged_in=is_logged_in, username=session.get('username'))

@app.route('/seeds_tools')
def seeds_tools():
    is_logged_in = 'username' in session
    return render_template('seeds_tools.html', is_logged_in=is_logged_in, username=session.get('username'))

@app.route('/meats')
def meats():
    is_logged_in = 'username' in session
    return render_template('meats.html', is_logged_in=is_logged_in, username=session.get('username'))

@app.route('/plus')
def plus():
    is_logged_in = 'username' in session
    return render_template('plus+.html', is_logged_in=is_logged_in, username=session.get('username'))


@app.route('/<page>.html')
def render_static_html(page):
    is_logged_in = 'username' in session
    try:
        return render_template(f"{page}.html", is_logged_in=is_logged_in, username=session.get('username'))
    except TemplateNotFound:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)