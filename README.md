# Online Store Template

## Description

This repository contains code for an online bookstore created by our team based on the ITSC 3155 template. the website displays list of items in stock but one must be logged in to place an order. A customer can log in using the login button or register a new user using the register button.

## How to Use

To run this project, you simply need to have Python 3.10 installed on your machine. You can download Python 3.10 from the [official website](<https://www.python.org/downloads/release/python-3108>). To complete each project milestone, OS-specific dependencies (such as `Graphviz` for generating UML diagrams) may need to be installed. These dependencies are listed in the project instructions.

### Setup and Installation

All module dependencies are listed in the `requirements.txt` file. To install these dependencies, run the following command from the root of the repository:

```bash
pip3 install -r requirements.txt
# Note: depending on your system, you may need to use `pip` or `python3.10 -m pip1 instead of `pip3`
```

### Database Setup

The project uses a SQLite database, which is stored in the `database` directory. To create or reset the database, navigate to the `database` directory and run the following command:

```bash
python3 ./database/reset_database.py
# Note: depending on your system, you may need to use `python3.10` or `py` instead of `python3`
```

### Running the Server

Once all installation steps are complete, the `app.py` script can be run to start the server. Follow the local server URL that is printed to the console to view the website.

## Documentation Style

Across all files, classes and functions are documented using docstrings, which are formatted according to the [Google Python Style Guide](<https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings>).

Additionally, detailed documents for the project code folders (`authentication`, `core`, `database`, `static` `templates`, and `tests`) have been provided in the `docs/directories` folder. These documents describe the purpose of each file in the folder and how they interact with each other.

## Testing

The unit tests are kept across various files in the `testing` directory. From the root of the repository, you can run the `test.py` script to check all unit tests, which will generate a report in the `testing/reports` directory.
