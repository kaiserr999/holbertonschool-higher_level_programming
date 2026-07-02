#!/usr/bin/python3
"""Flask app that loads products from JSON, CSV, or SQLite."""

import csv
import json
import os
import sqlite3

from flask import Flask, render_template, request


app = Flask(__name__)


def load_json_products(file_path):
    """Load products from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        return data.get('products', [])

    return []


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


def load_sql_products(file_path):
    """Load products from a SQLite database."""
    products = []

    conn = sqlite3.connect(file_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')

    for row in cursor.fetchall():
        products.append({
            'id': row['id'],
            'name': row['name'],
            'category': row['category'],
            'price': row['price']
        })

    cursor.close()
    conn.close()

    return products


def render_products(products_list, error=None):
    """Render the products template with optional error messaging."""
    return render_template('product_display.html', products=products_list, error=error)


@app.route('/products')
def products():
    """Render products from JSON, CSV, or SQLite source."""
    source = request.args.get('source', 'json')
    product_id = request.args.get('id')
    base_dir = os.path.dirname(__file__)

    try:
        if source == 'json':
            file_path = os.path.join(base_dir, 'products.json')
            products_list = load_json_products(file_path)
        elif source == 'csv':
            file_path = os.path.join(base_dir, 'products.csv')
            products_list = load_csv_products(file_path)
        elif source == 'sql':
            file_path = os.path.join(base_dir, 'products.db')
            products_list = load_sql_products(file_path)
        else:
            return render_products([], error='Wrong source')
    except (OSError, json.JSONDecodeError, sqlite3.Error, KeyError, ValueError):
        return render_products([], error='Database error')

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_products([], error='Product not found')

        products_list = [product for product in products_list if product.get('id') == product_id]

        if not products_list:
            return render_products([], error='Product not found')

    return render_products(products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)