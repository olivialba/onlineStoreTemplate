from database.db import Database

def test_admin_add_product() :
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