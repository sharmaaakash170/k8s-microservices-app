from flask import Flask, jsonify
import os
import redis
import psycopg2
import time

app = Flask(__name__)

r = redis.Redis(host=os.getenv('REDIS_HOST'), port=int(os.getenv('REDIS_PORT')), decode_responses=True)

def get_db_conn():
    return psycopg2.connect(
        host=os.getenv('POSTGRES_HOST', 'postgres'),
        database=os.getenv('POSTGRES_DB', 'admin'),
        user=os.getenv('POSTGRES_USER', 'admin'),
        password=os.getenv('POSTGRES_PASSWORD', 'admin')
    )

@app.route('/auth/ping')
def ping():
    return jsonify({'auth': 'pong'})

@app.route('/auth/redis')
def test_redis():
    r.set('auth-ping', 'pong')
    return jsonify({'redis': r.get('auth-ping')})

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/auth/db')
def test_db():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify({'postgres': db_version})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
