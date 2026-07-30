from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            category TEXT,
            quantity INTEGER,
            status INTEGER
        )
    ''')
    # Insert sample seed data
    cursor.execute("INSERT OR IGNORE INTO products VALUES ('123456789', 'Sample Product A', 'Test Category', 12, 1)")
    conn.commit()
    conn.close()

@app.route('/get_product_status', methods=['GET', 'POST'])
def get_product_status():
    product_id = request.args.get('product_id') or (request.json.get('product_id') if request.is_json else None)
    
    if not product_id:
        return jsonify({"error": "Missing product_id parameter"}), 400

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT product_id, title, category, quantity, status FROM products WHERE product_id = ?", (product_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify({
            "product_id": row[0],
            "title": row[1],
            "category": row[2],
            "quantity": row[3],
            "status": bool(row[4])
        }), 200
    else:
        return jsonify({"error": "Product not found", "status": False}), 404

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
  
