# Retail Inventory Management System

A Python-based retail inventory management project developed as part of my BSc (Hons) Computing studies.

The project explores backend application development, object-oriented programming, relational databases and REST-style API design using Python, Flask and MySQL.

## Project Objectives

The system was designed to demonstrate how a retail business could manage:

- Products and stock levels
- Users
- Purchases and sales
- Inventory transactions
- Database records
- Basic API access to product information

## Technologies

- Python
- Flask
- MySQL
- SQL
- REST-style APIs
- Object-Oriented Programming
- Git
- GitHub

## Database Design

The MySQL database contains three main entities:

### Users

Stores user account information.

### Products

Stores product details and current stock levels.

### Transactions

Records purchases and sales and links each transaction to a user and product.

This relational structure uses primary and foreign keys to maintain relationships between the data.

## Python and Object-Oriented Programming

The project includes a `Product` class that demonstrates object-oriented programming concepts.

Product stock can be updated through:

- `purchase()` – increases available stock
- `sell()` – reduces stock when sufficient inventory is available
- `get_stock()` – returns the current stock level

## Flask API

The project includes a Flask application with endpoints for retrieving product information.

Current example endpoints include:

```text
GET /products/
GET /products/<id>
```

The API returns product information in JSON format.

## Database Configuration

Database credentials are loaded from environment variables rather than being stored directly in the source code.

Create a local `.env` file using `.env.example` as a guide.

Example:

```text
DB_HOST=127.0.0.1
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=inventory_db
```

The `.env` file is excluded from Git version control.

## Project Structure

```text
retail-inventory-system/
│
├── app.py
├── products.py
├── users.py
├── transactions.py
├── db_config.py
├── create_database.sql
├── schema.sql
├── queries.sql
├── test_db.py
├── test_login.py
├── test_product.py
├── .env.example
├── .gitignore
└── README.md
```

## What I Learned

This project helped me develop practical experience with:

- Python application development
- Object-oriented programming
- SQL and relational database design
- MySQL connectivity
- Flask
- API development
- Database relationships
- Testing and debugging
- Git and GitHub
- Secure configuration practices

## Future Improvements

Potential future development includes:

- Connecting all Flask endpoints directly to the MySQL database
- Adding complete CRUD functionality
- Implementing authentication
- Improving validation and error handling
- Developing a web-based user interface
- Adding inventory reporting and analytics

## About Me

I'm a BSc (Hons) Computing student at the University of Central Lancashire, graduating in August 2027, with a particular interest in Business Intelligence, Data Analytics and data-driven decision-making.
