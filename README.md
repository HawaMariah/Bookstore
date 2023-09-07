# Miss Mariah's Bookstore

Miss Mariah's Bookstore is a command-line interface (CLI) application for managing a bookstore's inventory, processing orders, and facilitating book exchanges.

## Features
- Search and Buy Books: Users can search for books by title, view their details (author, price, quantity), and make purchases.

- Sort by Price: Users can sort available books by price to help them find the best deals.

- Exchange Books: Users can exchange their own books for store credit.

- User Registration: New users can register with their first name, last name, email address, and phone number.

## Dependencies
- sqlalchemy: An SQL toolkit and Object-Relational Mapping (ORM) system for Python.

- alembic: A database migration tool for SQLAlchemy.

## Installation
- Clone the repository:
git clone https://github.com/yourusername/bookstore.git
- change directory- bookstore
- Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  
-Install the dependencies:
pip install -r requirements.txt
-Create a database and tables using Alembic:
alembic upgrade head

## Usage
- Run the application:
python search.py
- Follow the prompts to register as a user and start using the bookstore.

## Database Management
- To create a new migration after making changes to your models, use:
alembic revision --autogenerate -m "description of changes"
- To apply the new migration, use:
alembic upgrade head

## License
This project is licensed under the MIT License. See the LICENSE file for details.




