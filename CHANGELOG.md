# Changelog

## **Changes by Alberto**
### Website:
- Added `Admin Panel`
- Added Header
- Added Logout
- Added login and register buttons
- Added Homepage navbar
- Added customers can't register with 'admin' in their username
- Added backend for login-register-logout

### Admin Panel:
- Bookstoremanager login will show an Admin panel, the panel is defined in 'admin_panel.html' and 'admin_panel.py'
- Bookstoremanager login info: 
  - Username: `Admin`
  - Password: `Admin`
- Admin Panel functionalities added:
  - Add New Product to add items into the database
  - Update Product to update all fields in an item into the database

### Fixed Bugs:
- Fixed: login users didn't change session to their new login
- Fixed: customers can't login if username or password invalid
- Fixed: incorrect and uneven css style for login and register .html pages