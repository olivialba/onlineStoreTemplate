from authentication.auth_tools import login_pipeline, update_passwords, hash_password
from flask import Blueprint, Flask, render_template, request
from core_info import sessions, db

admin_panel_bp = Blueprint('admin_panel', __name__)

@admin_panel_bp.route('/add-product', methods=['POST'])
def add_product():
    item_name = request.form['itemname']
    price = request.form['price']
    info = request.form['info']
    stock = request.form['stock']
    image_url = request.form['image_url']
    category = request.form['category']
    db.insert_new_item(item_name, price, info, stock, image_url, category)
    return render_template('admin_panel.html')