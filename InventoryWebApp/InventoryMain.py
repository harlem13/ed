from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client.EdMongoDB


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/inventory', methods=['GET'])
def get_inventory():
    try:
        inventory = []
        for item in db.InventoryApp.find():
            inventory.append({
                'name': item['name'],
                'quantity': item['quantity'],
                'unit': item['unit']
            })
        return jsonify(inventory)
    except PyMongoError as e:
        return jsonify({'error': str(e)}), 500


@app.route('/inventory', methods=['POST'])
def add_item():
    try:
        name = request.json['name']
        quantity = request.json['quantity']
        unit = request.json['unit']
        if not name:
            return jsonify({'error': 'Name is required'}), 400
        if not isinstance(quantity, int):
            return jsonify({'error': 'Quantity must be an integer'}), 400
        if not unit:
            return jsonify({'error': 'Unit is required'}), 400
        db.InventoryApp.insert_one({'name': name, 'quantity': quantity, 'unit': unit})
        return jsonify({'message': 'Item added successfully'})
    except KeyError:
        return jsonify({'error': 'Name, quantity, and unit are required in the request body'}), 400
    except PyMongoError as e:
        return jsonify({'error': str(e)}), 500


@app.route('/inventory/<name>', methods=['PUT'])
def update_item(name):
    try:
        quantity = request.json['quantity']
        unit = request.json['unit']
        if not isinstance(quantity, int):
            return jsonify({'error': 'Quantity must be an integer'}), 400
        result = db.InventoryApp.update_one({'name': name}, {'$set': {'quantity': quantity, 'unit': unit}})
        if result.matched_count == 0:
            return jsonify({'error': f"No item found with name '{name}'"}), 404
        return jsonify({'message': 'Item updated successfully'})
    except KeyError:
        return jsonify({'error': 'Quantity and unit are required in the request body'}), 400
    except PyMongoError as e:
        return jsonify({'error': str(e)}), 500


@app.route('/inventory/<name>', methods=['DELETE'])
def delete_item(name):
    try:
        result = db.InventoryApp.delete_one({'name': name})
        if result.deleted_count == 0:
            return jsonify({'error': f"No item found with name '{name}'"}), 404
        return jsonify({'message': 'Item deleted successfully'})
    except PyMongoError as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
