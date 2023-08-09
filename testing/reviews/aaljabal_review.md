Tests performed:

auth_tests.py
core_tests.py
db_tests.py

After performing the following tests auth_tests.py all tests suceeded but core and db tests all failed.
After taking a closer look at the tests and at the project i found out the tests had a bug, in which i managed to fix by updating the database path.
After the edit all tests suceeded.

Did manual testing too where i tested all kind of wrong input, logging in, registration and adding to the cart. no issues were found and website has full functionality.

Recommend adding more tests regarding core_tests especially backend routes if changing users will affect the cart.
