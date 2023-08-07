from core.session import Sessions
from core.utils import admin_add_new_item
from database.db import Database

db = Database('database/store_records.db') # Database
sessions = Sessions() # Sessions