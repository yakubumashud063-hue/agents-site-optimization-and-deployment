from flask import Flask, render_template, request, redirect, url_for, abort, session, jsonify
from jinja2 import TemplateNotFound
from functools import wraps
from werkzeug.utils import secure_filename
import json
import time
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'farmfresh_secret_key_2025'

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


def infer_price_from_name(name, category):
    base = sum(ord(c) for c in name) % 100
    if category == 'Fruits':
        price = 3 + (base % 15)
    elif category == 'Vegetables':
        price = 2 + (base % 12)
    elif category == 'Dairy':
        price = 4 + (base % 8)
    elif category == 'Livestock':
        price = 40 + (base % 120)
    elif category == 'Meats':
        price = 15 + (base % 40)
    else:
        price = 5 + (base % 20)
    return f"{price:.2f}"


def load_products():
    if products_file.exists():
        products = json.loads(products_file.read_text())
    else:
        products = [
            {
                'id': 1,
                'name': 'Organic Tomatoes',
                'price': '4.50',
                'description': 'Fresh farm tomatoes, juicy and rich in flavor.',
                'category': 'Vegetables',
                'image_url': '/static/images/Tomatoes.png',
                'uploaded_by': 'FarmFresh'
            },
            {
                'id': 2,
                'name': 'Sweet Bananas',
                'price': '7.50',
                'description': 'Ripe bananas perfect for smoothies and snacks.',
                'category': 'Fruits',
                'image_url': '/static/images/Banana.jpg',
                'uploaded_by': 'FarmFresh'
            },
            {
                'id': 3,
                'name': 'Free-Range Eggs',
                'price': '6.00',
                'description': 'Large, farm-fresh eggs from healthy chickens.',
                'category': 'Dairy',
                'image_url': '/static/images/egg plant.jpg',
                'uploaded_by': 'FarmFresh'
            }
        ]

    existing_images = {Path(product.get('image_url', '')).name.lower() for product in products}
    next_id = max((product.get('id', 0) for product in products), default=0) + 1
    new_products = []

    for image_path in sorted((Path(__file__).parent / 'static' / 'images').glob('*')):
        if not image_path.is_file() or image_path.suffix.lower().lstrip('.') not in ALLOWED_EXTENSIONS:
            continue

        image_name = image_path.name.lower()
        if image_name in existing_images:
            continue

        product_name = image_path.stem.replace('_', ' ').replace('-', ' ').title()
        category = infer_category_from_filename(product_name)
        product = {
            'id': next_id,
            'name': product_name,
            'price': infer_price_from_name(product_name, category),
            'description': f'Fresh {product_name} from FarmFresh.',
            'category': category,
            'image_url': f'/static/images/{image_path.name}',
            'uploaded_by': 'FarmFresh'
        }
        products.append(product)
        new_products.append(product)
        existing_images.add(image_name)
        next_id += 1

    if new_products:
        save_products(products)

    return products


def save_products(products):
    products_file.write_text(json.dumps(products, indent=2))

# Message storage helpers

def load_messages():
    if messages_file.exists():
        return json.loads(messages_file.read_text())
    return []


def save_messages(items):
    messages_file.write_text(json.dumps(items, indent=2))

# Order storage helpers

def load_orders():
    if orders_file.exists():
        return json.loads(orders_file.read_text())
    return []


def save_orders(orders):
    orders_file.write_text(json.dumps(orders, indent=2))

# Cart helpers

def get_cart_items():
    cart = session.get('cart', [])
    products = load_products()
    items = []
    total = 0.0

    for entry in cart:
        product = next((p for p in products if p['id'] == entry.get('product_id')), None)
        if not product:
            continue
        quantity = int(entry.get('quantity', 1))
        subtotal = round(float(product['price']) * quantity, 2)
        items.append({
            'product_id': product['id'],
            'name': product['name'],
            'price': product['price'],
            'description': product['description'],
            'category': product['category'],
            'image_url': product['image_url'],
            'uploaded_by': product['uploaded_by'],
            'quantity': quantity,
            'subtotal': f"{subtotal:.2f}"
        })
        total += subtotal

    return items, round(total, 2)


def cart_item_count():
    return sum(int(item.get('quantity', 0)) for item in session.get('cart', []))


def get_current_user():
    username = session.get('username')
    if not username:
        return None
    users = load_users()
    return users.get(username)


def is_admin_user():
    user = get_current_user()
    return bool(user and user.get('role') == 'admin')


def find_user_by_username_or_email(identifier):
    users = load_users()
    if not identifier:
        return None, None
    if identifier in users:
        return identifier, users[identifier]
    target = identifier.lower().strip()
    for username, user in users.items():
        if username.lower() == target or user.get('email', '').lower() == target:
            return username, user
    return None, None


def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def require_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        if not is_admin_user():
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function


@app.context_processor
def inject_user_context():
    return {
        'is_logged_in': 'username' in session,
        'username': session.get('username'),
        'is_admin': is_admin_user(),
        'cart_count': cart_item_count()
    }

# Route for the homepage
@app.route('/')
def home():
    is_logged_in = 'username' in session
    featured_products = load_products()[:6]
    return render_template(
        'template.html',
        is_logged_in=is_logged_in,
        username=session.get('username'),
        featured_products=featured_products,
        cart_count=cart_item_count()
    )

# User Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        email = request.form.get('email')

        if not username or not password or not email:
            return render_template('register.html', error='Username, email, and password are required')

        if password != confirm_password:
            return render_template('register.html', error='Passwords do not match')

        users = load_users()
        if username in users:
            return render_template('register.html', error='Username already exists')

        admin_usernames = {'admin', 'mashud'}
        role = 'admin' if username.lower() in admin_usernames else 'user'
        users[username] = {'password': password, 'email': email, 'role': role}
        save_users(users)
        session['username'] = username
        return redirect(url_for('home'))

    is_logged_in = 'username' in session
    return render_template('register.html', is_logged_in=is_logged_in, username=session.get('username'))

# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        username, user = find_user_by_username_or_email(identifier)
        if user and user.get('password') == password:
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
    category = request.form.get('product-category', 'Other')
    image = request.files.get('product-image')

    if not product_name or not price:
        return jsonify({'error': 'Product name and price required'}), 400

    if not image or image.filename == '':
        return jsonify({'error': 'Product image is required'}), 400

    if not allowed_file(image.filename):
        return jsonify({'error': 'Invalid image type. Use png, jpg, jpeg, or gif.'}), 400

    filename = secure_filename(f"{int(time.time())}_{session['username']}_{image.filename}")
    image_path = uploads_dir / filename
    image.save(image_path)
    image_url = url_for('static', filename=f'uploads/{filename}')

    products = load_products()
    new_product = {
        'id': len(products) + 1,
        'name': product_name,
        'price': price,
        'description': description,
        'category': category,
        'image_url': image_url,
        'uploaded_by': session.get('username')
    }
    products.insert(0, new_product)
    save_products(products)

    return jsonify({'success': True, 'message': f'Product "{product_name}" uploaded successfully!', 'product': new_product})

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

@app.route('/fruits')
def fruits():
    category_products = [product for product in load_products() if product.get('category', '').lower() == 'fruits']
    return render_template('fruits.html', category_name='Fruits', category_products=category_products)

@app.route('/vegetables')
def vegetables():
    category_products = [product for product in load_products() if product.get('category', '').lower() == 'vegetables']
    return render_template('vegetables.html', category_name='Vegetables', category_products=category_products)

@app.route('/products')
def products_page():
    is_logged_in = 'username' in session
    return render_template(
        'products.html',
        is_logged_in=is_logged_in,
        username=session.get('username'),
        products=load_products(),
        cart_count=cart_item_count()
    )

@app.route('/dashboard')
@require_login
def dashboard():
    username = session.get('username')
    user_orders = [order for order in load_orders() if order.get('user') == username]
    user_products = [product for product in load_products() if product.get('uploaded_by') == username]
    clients = sorted({order.get('email') for order in user_orders if order.get('email')})
    notifications = [
        f"Order #{order.get('order_id')} is {order.get('status', 'Pending')}",
        f"You have {len(user_products)} active listing(s) on the platform."
    ] if user_orders or user_products else ["No new notifications."]
    return render_template(
        'dashboard.html',
        is_logged_in=True,
        username=username,
        orders=user_orders,
        products=user_products,
        clients=clients,
        notifications=notifications,
        cart_count=cart_item_count()
    )

@app.route('/orders')
@require_login
def orders_page():
    username = session.get('username')
    orders = [order for order in load_orders() if order.get('user') == username]
    return render_template(
        'orders.html',
        is_logged_in=True,
        username=username,
        orders=orders,
        cart_count=cart_item_count()
    )

@app.route('/profile/<target_username>')
@require_login
def profile_page(target_username):
    current_username = session.get('username')
    users = load_users()
    if target_username not in users:
        abort(404)

    if current_username != target_username and not is_admin_user():
        abort(403)

    profile_user = users[target_username]
    user_orders = [order for order in load_orders() if order.get('user') == target_username]
    user_products = [product for product in load_products() if product.get('uploaded_by') == target_username]
    clients = sorted({order.get('email') for order in user_orders if order.get('email')})
    messages = [message for message in load_messages() if message.get('email', '').lower() == profile_user.get('email', '').lower()]
    return render_template(
        'user_profile.html',
        profile_username=target_username,
        profile_user=profile_user,
        user_orders=user_orders,
        user_products=user_products,
        clients=clients,
        messages=messages,
        is_own_profile=current_username == target_username,
        is_admin_view=current_username != target_username and is_admin_user(),
        cart_count=cart_item_count()
    )

@app.route('/admin', methods=['GET', 'POST'])
@require_admin
def admin_page():
    is_logged_in = 'username' in session
    username = session.get('username')
    products = load_products()
    orders = load_orders()
    users = load_users()
    message = None
    user_profiles = []
    for user_name, user_data in users.items():
        user_profiles.append({
            'username': user_name,
            'email': user_data.get('email', ''),
            'role': user_data.get('role', 'user'),
            'active': user_data.get('active', True),
            'orders': len([order for order in orders if order.get('user') == user_name]),
            'ads': len([product for product in products if product.get('uploaded_by') == user_name])
        })
    total_sales = sum(float(order.get('total', 0) or 0) for order in orders)
    low_stock_products = [product for product in products if int(product.get('stock_quantity', 0)) <= 5]

    if request.method == 'POST':
        action = request.form.get('action')
        product_id = int(request.form.get('product_id', 0))

        if action == 'delete' and product_id:
            products = [product for product in products if product['id'] != product_id]
            save_products(products)
            return redirect(url_for('admin_page'))

        if action == 'update' and product_id:
            for product in products:
                if product['id'] == product_id:
                    product['name'] = request.form.get('name', product['name'])
                    product['price'] = request.form.get('price', product['price'])
                    product['description'] = request.form.get('description', product['description'])
                    product['category'] = request.form.get('category', product['category'])
                    product['status'] = request.form.get('status', product.get('status', 'Published'))
                    product['stock_quantity'] = int(request.form.get('stock_quantity', product.get('stock_quantity', 0)))
                    break
            save_products(products)
            return redirect(url_for('admin_page'))

        if action == 'create':
            name = request.form.get('name')
            price = request.form.get('price')
            category = request.form.get('category', 'Other')
            description = request.form.get('description', '')
            status = request.form.get('status', 'Published')
            stock_quantity = int(request.form.get('stock_quantity', 0))
            if name and price:
                new_id = max([p['id'] for p in products], default=0) + 1
                products.insert(0, {
                    'id': new_id,
                    'name': name,
                    'price': price,
                    'description': description,
                    'category': category,
                    'status': status,
                    'stock_quantity': stock_quantity,
                    'image_url': '/static/images/logo.png',
                    'uploaded_by': username
                })
                save_products(products)
                return redirect(url_for('admin_page'))
            message = 'Product name and price are required.'

        if action == 'order_update':
            order_id = int(request.form.get('order_id', 0))
            status = request.form.get('status', 'Pending')
            for order in orders:
                if order.get('order_id') == order_id:
                    order['status'] = status
                    break
            save_orders(orders)
            return redirect(url_for('admin_page'))

        if action == 'toggle_user_active':
            target_username = request.form.get('target_username')
            if target_username in users:
                users[target_username]['active'] = not users[target_username].get('active', True)
                save_users(users)
            return redirect(url_for('admin_page'))

    return render_template(
        'admin.html',
        is_logged_in=is_logged_in,
        username=username,
        products=products,
        orders=orders,
        users_count=len(users),
        orders_count=len(orders),
        total_sales=f"{total_sales:.2f}",
        low_stock_products=low_stock_products,
        cart_count=cart_item_count(),
        message=message,
        user_profiles=user_profiles
    )

@app.route('/cart')
def cart_page():
    is_logged_in = 'username' in session
    cart_items, total = get_cart_items()
    return render_template(
        'cart.html',
        is_logged_in=is_logged_in,
        username=session.get('username'),
        cart_items=cart_items,
        total=f"{total:.2f}",
        cart_count=cart_item_count()
    )

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json() or request.form
    product_id = int(data.get('product_id', 0))
    if not product_id:
        return jsonify({'error': 'Invalid product id'}), 400

    cart = session.get('cart', [])
    for entry in cart:
        if entry.get('product_id') == product_id:
            entry['quantity'] = int(entry.get('quantity', 1)) + 1
            break
    else:
        cart.append({'product_id': product_id, 'quantity': 1})

    session['cart'] = cart
    return jsonify({'success': True, 'cart_count': cart_item_count()})

@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    data = request.get_json() or request.form
    product_id = int(data.get('product_id', 0))
    cart = session.get('cart', [])
    cart = [entry for entry in cart if entry.get('product_id') != product_id]
    session['cart'] = cart
    return jsonify({'success': True, 'cart_count': cart_item_count()})

@app.route('/checkout', methods=['GET', 'POST'])
@require_login
def checkout():
    is_logged_in = 'username' in session
    cart_items, total = get_cart_items()
    if not cart_items:
        return redirect(url_for('cart_page'))

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        address = request.form.get('address')
        phone = request.form.get('phone')
        payment_method = request.form.get('payment_method', 'Cash on delivery')
        card_name = request.form.get('card_name', '').strip()
        card_number = request.form.get('card_number', '').strip()
        expiry = request.form.get('expiry', '').strip()
        cvv = request.form.get('cvv', '').strip()

        if payment_method == 'Card':
            if not card_name or not card_number or not expiry or not cvv:
                return render_template(
                    'checkout.html',
                    is_logged_in=is_logged_in,
                    username=session.get('username'),
                    cart_items=cart_items,
                    total=f"{total:.2f}",
                    error='Card payment requires cardholder name, card number, expiry date, and CVV.',
                    cart_count=cart_item_count()
                )

        if not name or not email or not address or not phone:
            return render_template(
                'checkout.html',
                is_logged_in=is_logged_in,
                username=session.get('username'),
                cart_items=cart_items,
                total=f"{total:.2f}",
                error='All checkout fields are required.',
                cart_count=cart_item_count()
            )

        orders = load_orders()
        order = {
            'order_id': int(time.time()),
            'customer': name,
            'email': email,
            'phone': phone,
            'address': address,
            'items': cart_items,
            'total': f"{total:.2f}",
            'status': 'Pending',
            'payment_method': payment_method,
            'payment_reference': card_number[-4:] if payment_method == 'Card' and card_number else 'Cash-on-delivery',
            'user': session.get('username'),
            'created_at': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        orders.insert(0, order)
        save_orders(orders)
        session['cart'] = []

        return render_template(
            'checkout.html',
            is_logged_in=is_logged_in,
            username=session.get('username'),
            cart_items=[],
            total='0.00',
            success='Order completed successfully!',
            order=order,
            cart_count=cart_item_count()
        )

    return render_template(
        'checkout.html',
        is_logged_in=is_logged_in,
        username=session.get('username'),
        cart_items=cart_items,
        total=f"{total:.2f}",
        cart_count=cart_item_count()
    )

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    is_logged_in = 'username' in session
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            return render_template(
                'contact.html',
                is_logged_in=is_logged_in,
                username=session.get('username'),
                error='Please fill in all fields.',
                cart_count=cart_item_count()
            )

        messages = load_messages()
        messages.insert(0, {
            'name': name,
            'email': email,
            'message': message,
            'submitted_at': time.strftime('%Y-%m-%d %H:%M:%S')
        })
        save_messages(messages)

        return render_template(
            'contact.html',
            is_logged_in=is_logged_in,
            username=session.get('username'),
            success='Your message has been received. We will respond soon.',
            cart_count=cart_item_count()
        )

    return render_template(
        'contact.html',
        is_logged_in=is_logged_in,
        username=session.get('username'),
        cart_count=cart_item_count()
    )

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