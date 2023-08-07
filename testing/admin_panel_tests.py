from database.db import Database
from core.utils import admin_add_new_item

""" 
DESCRIPTION:
This script is similar to the `auth_tests.py` file.
Functions used in the admin_panel.py, that admin accounts use to manage the database, are tested to see if they work correctly. 
Test by Alberto Olivi

NOTE: It's important that a database already exists to test these functions, as these functions works directly with it. 
You need to use `python3 database/reset_database.py` to create the database if not already done.
"""


def test_admin_add_product():
    """
    Tests that you can successfully add items into the database using the admin_panel function.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """
    db = Database("database/store_records.db")
    
    item_name = "test_itemname"
    price = "1.2"
    info = "test_info"
    stock = "3"
    image_url = "test_image_url"
    category = "test_category"
    
    success, message = admin_add_new_item(db, item_name, price, info, stock, image_url, category)
    if success:
        negative_value, message = admin_add_new_item(db, item_name, "-1.2", info, stock, image_url, category)
        if not negative_value:
            not_integer, message = admin_add_new_item(db, item_name, price, info, "e", image_url, category)
            if not not_integer:
                return True, "Item successfully added."
            else:
                return False, "ERROR: Item was added successfully even though stock is not an integer."
        else:
            return False, "ERROR: Item was added successfully even though price is negative."
    else:
        return False, message