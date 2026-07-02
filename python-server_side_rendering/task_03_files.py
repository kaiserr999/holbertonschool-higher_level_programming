#!/usr/bin/python3
"""Flask app that loads products from JSON or CSV files."""

import csv
import json
import os

from flask import Flask, abort, render_template, request


app = Flask(__name__)


def load_json_products(file_path):
    """Load products from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data.get('products', [])


def load_csv_products(file_path):
    """Load products from a CSV file."""
    products = []

    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })

    return products


@app.route('/products')
def products():
    """Render products from JSON or CSV source."""
    source = request.args.get('source', 'json')
    product_id = request.args.get('id')
    base_dir = os.path.dirname(__file__)

    if source == 'json':
        file_path = os.path.join(base_dir, 'products.json')
        products_list = load_json_products(file_path)
    elif source == 'csv':
        file_path = os.path.join(base_dir, 'products.csv')
        products_list = load_csv_products(file_path)
    else:
        abort(404, description='Source not found')

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            abort(404, description='Product not found')

        products_list = [product for product in products_list if product.get('id') == product_id]

        if not products_list:
            abort(404, description='Product not found')

    return render_template('product_display.html', products=products_list, source=source)


if __name__ == '__main__':
    app.run(debug=True, port=5000)