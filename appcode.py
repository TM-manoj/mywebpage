from flask import Flask, request, jsonify
import os
import pymysql  # or psycopg2 if using Postgres

app = Flask(__name__)

# Read DB credentials from environment (never hard-code in code)
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')

def get_db_conn():
    return pymysql.connect(host=DB_HOST,
                           user=DB_USER,
                           password=DB_PASS,
                           database=DB_NAME)

@app.route('/signup', methods=['POST'])
def signup():
    body = request.get_json()
    name = body.get('name')
    if not name:
        return jsonify({"message": "Name required"}), 400

    conn = get_db_conn()
    try:
        with conn.cursor() as c:
            c.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        conn.commit()
    finally:
        conn.close()
    return jsonify({"message": f"User {name} signed up!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
