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
- Git / GitHub

## Database Design

The MySQL database contains three main entities:

### Users
Stores user account information.

### Products
Stores product details and current stock levels.

### Transactions
Records purchases and sales and links each transaction to a user and product.

This relational structure uses primary and foreign keys to maintain relationships between the data.

## Python & OOP

The project includes a `Product` class that demonstrates object-oriented programming concepts such as encapsulation.

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
