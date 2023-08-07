import sqlite3
import uuid


def dict_factory(cursor: sqlite3.Cursor, row: tuple) -> dict:
    """
    Creates a dictionary from a row in the database. This is used to convert the rows into dictionaries.

    args:
        - cursor: The cursor of the database, which is a built-in sqlite3 class.
        - row: The row to convert into a dictionary.

    returns:
        - The dictionary of the row.
    """

    row_dict = {}
    for index, column in enumerate(cursor.description):
        row_dict[column[0]] = row[index]
    return row_dict


def calculate_cost(price: int, quantity: int, discount: float = 0.0, tax_rate: float = 0.05) -> float:
    """
    Calculates the cost of an item.

    args:
        - price: The price of the item.
        - quantity: The quantity of the item.
        - discount: The discount of the item.
        - tax_rate: The tax rate of the item.

    returns:
        - The cost of the item as a float.
    """
    subtotal = (price * quantity) * (1 - discount) * (1 + tax_rate)
    return round(subtotal, 2)


def calculate_total_cost(items: dict) -> float:
    """
    Calculates the total cost of a set of items.

    args:
        - items: A dictionary of items to calculate the total cost of.

    returns:
        - The total cost of the sale as a float.
    """
    total_cost = 0
    #print(items)
    for i in items:
        item = items[i]
        total_cost += calculate_cost(float(item["price"]), int(item["quantity"]),
                                     float(item["discount"]), float(item["tax_rate"]))
    return round(total_cost, 2)


def generate_unique_id() -> str:
    """
    Generates a unique ID.

    args:
        - None

    returns:
        - A unique ID as a string.
    """
    return str(uuid.uuid4())

def generate_transaction_id(length) -> str:
    """
    Generates a unique transaction ID with 5 characters.

    args:
        - None

    returns:
        - A unique transaction ID as a string.
    """
    return str(uuid.uuid4())[:length]

def check_float(value: str):
    """
    Check if a value can become a float

    args:
        - value

    returns:
        - Whether the value can be converted to a float or not
    """
    try:
        value = float(value)
        return value
    except ValueError:
        return None

def admin_add_new_item(db, item_name: str, price: str, info: str, stock: str, image_url: str, category: str):
    """
    Add a new item into the database from admin_panel

    args:
        - item_name
        - price
        - info
        - stock
        - image_url
        - category

    returns:
        - Whether the item was successfully added
    """
    if not item_name or not price or not info or not stock or not image_url or not category:
        return False, "One or more fields are missing."
    
    price_float = check_float(price)
    stock_float = check_float(stock)
    if price_float is None or stock_float is None:
        return False, "Price or stock value is not a valid float."
    
    if not stock_float.is_integer():
        return False, "Stock value is not an integer."
    
    if price_float < 0 or stock_float < 0:
        return False, "Price or stock can't be negative."
    
    db.insert_new_item(item_name, price, info, stock, image_url, category)
    return True, "Item successfully added."