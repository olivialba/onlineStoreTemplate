# Admin Panel by Alberto Olivi

from authentication.auth_tools import login_pipeline, update_passwords, hash_password
from flask import Blueprint, Flask, render_template, request
from core_info import sessions, db, admin_add_new_item

admin_panel_bp = Blueprint('admin_panel', __name__) 

"""
Used to update product info
First is textfield from which to take value, second is method to use to update said value
"""
field_to_db_update = {
    'itemname_update': db.set_item_name,
    'info_update': db.set_item_info,
    'price_update': db.set_item_price,
    'stock_update': db.set_item_stock,
    'image_url_update': db.set_item_image_url,
    'category_update': db.set_item_category
}


@admin_panel_bp.route('/admin_panel/add-product', methods=['POST'])
def add_product():
    """
    Renders the add-product request when the user is at the `/admin_panel/add-product` endpoint with a POST request.
    Add product to the database.

    args:
        - None

    returns:
        - None

    modifies:
        - database/store_records.db: add a product to the inventory in the database.
    """
    item_name = request.form['itemname']
    price = request.form['price']
    info = request.form['info']
    stock = request.form['stock']
    image_url = request.form['image_url']
    category = request.form['category']
    
    success, message = admin_add_new_item(db, item_name, price, info, stock, image_url, category)
    if success:
        print(message)
        return render_template('admin_panel.html', product_added=True)
    else:
        print("Error: ", message)
        return render_template('admin_panel.html', error_message=message)


@admin_panel_bp.route('/admin_panel/update-product', methods=['POST'])
def update_product():
    """
    Renders the update-product page when the user is at the `/admin_panel/update-product` endpoint with a POST request.
    Shows product data and allows for product data to be edited in the database.

    args:
        - None

    returns:
        - Data: shows product's data in the /update-product page

    modifies:
        - database/store_records.db: change a product data
    """
    
    # Button to search for product in database
    if 'button_send' in request.form and request.form['button_send'] == 'find_product':
        item_id = request.form['itemid']
        return render_item_info(item_id)
    
    # Button to update a product in database
    elif 'button_send' in request.form and request.form['button_send'] == 'update_product':
        item_id = request.form['id_update']
        for field, update_info in field_to_db_update.items():
            new_value = request.form[field].strip()
            if new_value:
                update_info(item_id, new_value)
        return render_item_info(item_id)
    
    else:
        print('Error: Could not detect button pressed. How were you even able to cause this error?')
        return render_template('admin_panel.html')
    

@admin_panel_bp.route('/admin_panel/view-inventory', methods=['POST'])
def view_inventory():
    """
    Renders the inventory products when the user is at the `/admin_panel/view-inventory` endpoint with a POST request.
    With 'GET' you can go directly to the url even without admin access or log in?
    
    args:
        - None

    returns:
        - None
    """
    inventory = db.get_full_inventory()
    return render_template('admin_panel.html', inventory=inventory)



def render_item_info(item_id: int):
    """
    Get all the product data corresponding to the product item_id from the database.
    Used to display data for the 'Update Product' panel

    args:
        - item_id: integer for product id

    returns:
        - Render admin_panel page with product/item information
    """
    check = db.get_item_name_by_id(item_id)
    
    # Couldn't find item ID in database, send item_not_found error
    if check is None:
        return render_template('admin_panel.html', item_not_found=True)
    
    name = check['item_name']
    info = db.get_item_info_by_id(item_id)['info']
    price = db.get_item_price_by_id(item_id)['price']
    stock = db.get_item_stock_by_id(item_id)['stock']
    image_url = db.get_item_image_url_by_id(item_id)['image_url']
    category = db.get_item_category_by_id(item_id)['category']
    return render_template('admin_panel.html', item_found=True, item_id=item_id, name=name, info=info, price=price, stock=stock, image_url=image_url, category=category)