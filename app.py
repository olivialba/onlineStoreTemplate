#!/usr/bin/env python3

from authentication.auth_tools import login_pipeline, update_passwords, hash_password
from flask import Flask, render_template, request
from admin_panel import admin_panel_bp
from core_info import sessions, db # Sessions and Database

app = Flask(__name__)
app.register_blueprint(admin_panel_bp) # Register blueprint to connect 'app.py' to 'admin_panel.py'
HOST, PORT = 'localhost', 8080
global username, products, db, sessions
username = 'default'
products = db.get_full_inventory()
sessions.add_new_session(username, db)


@app.route('/')
def index_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    products = db.get_full_inventory() # Reload Inventory in case a new product was just added
    print(username)
    print(sessions.get_all_sessions())
    if username != 'default': # If a user is logged in, re-route to show home.html
        return render_template('home.html', username=username, products=products, sessions=sessions)
    return render_template('index.html', username=username, products=products, sessions=sessions)


@app.route('/login')
def login_page():
    """
    Renders the login page when the user is at the `/login` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('login.html')


@app.route('/home', methods=['POST'])
def login():
    """
    Renders the home page when the user is at the `/home` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds a new session to the sessions object

    """
    user = request.form['username']
    password = request.form['password']
    if login_pipeline(user, password):
        global username
        sessions.remove_session(username) # Remove previous session
        sessions.add_new_session(user, db) # Add new session
        username = user # Set global username of new session
        if user == 'Admin':
            print(f"Special username logged in: {user}")
            return render_template('home.html', username=user, products=products, sessions=sessions)
        else: 
            return render_template('home.html', products=products, sessions=sessions)
    else:
        print(f"Incorrect username ({user}) or password ({password}).")
        return render_template('index.html')


@app.route('/register')
def register_page():
    """
    Renders the register page when the user is at the `/register` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    """
    Renders the index page when the user is at the `/register` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - passwords.txt: adds a new username and password combination to the file
        - database/store_records.db: adds a new user to the database
    """
    username = request.form['username']
    # ERROR: Customers can't have 'admin' in their username
    if 'admin' in username.lower():
        return render_template('register.html', admin_error=True)
    
    password = request.form['password']
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    salt, key = hash_password(password)
    update_passwords(username, key, salt)
    db.insert_user(username, key, email, first_name, last_name)
    return render_template('index.html')


@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Renders the checkout page when the user is at the `/checkout` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds items to the user's cart
    """
    order = {}
    user_session = sessions.get_session(username)
    for item in products:
        print(f"item ID: {item['id']}")
        if request.form[str(item['id'])] > '0':
            count = request.form[str(item['id'])]
            order[item['item_name']] = count
            user_session.add_new_item(
                item['id'], item['item_name'], item['price'], count)

    user_session.submit_cart()

    return render_template('checkout.html', order=order, sessions=sessions, total_cost=user_session.total_cost)

@app.route('/admin_panel', methods=['POST'])
def admin_panel():
    all_sessions = sessions.get_all_sessions()
    for username in all_sessions:
        if 'admin' in username.lower():
            print("Admin verified: proceeding to Admin Panel")
            return render_template('admin_panel.html', sessions=sessions)
    return render_template('index.html', username=username, products=products, sessions=sessions)

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
