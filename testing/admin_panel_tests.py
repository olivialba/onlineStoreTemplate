from database.db import Database
from core.utils import admin_add_new_item

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
        return True, message
    else:
        return False, message