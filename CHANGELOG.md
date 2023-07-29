# P3 Implementation Changelog

## **Changes by Alberto**
### Website:
- Added `Admin Panel`
- Added Header
- Added Logout
- Added Homepage navbar
- Added Checkout Page table with cart table info
- Added users can update quantity of items at checkout
- Added Books products to starting_data
- Changed overall CSS style of the website
- Changed Login and Register buttons

### Admin Panel:
- Bookstoremanager login will show an Admin panel, the panel is defined in 'admin_panel.html' and 'admin_panel.py'
- Bookstoremanager login info: 
  - Username: `Admin`
  - Password: `Admin`
- Admin Panel functionalities added:
  - Add New Product to add items into the database
  - Update Product to update all fields in an item into the database

### Fixed Bugs:
- Prevent: users can't register with 'default' or 'admin' in their username, to prevent bugs
- Fixed: login users didn't change session to their new login
- Fixed: customers can't login if username or password invalid
- Fixed: incorrect and uneven css style for login and register .html pages
- Fixed: Incorrect backend for login-logout
- Fixed: Users now keep their cart saved even after logging out
