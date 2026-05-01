from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Retail Inventory Management System"

@app.route('/products/', methods=['GET'])
def get_products():
    products = [
        {'id': 1, 'name': 'Mobile Phone'},
        {'id': 2, 'name': 'Laptop'}
    ]
    return jsonify(products)

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    products = [
        {'id': 1, 'name': 'Mobile Phone'},
        {'id': 2, 'name': 'Laptop'}
    ]

    for product in products:
        if product['id'] == id:
            return jsonify(product)

    return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)