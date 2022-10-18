from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate
from dataclasses import dataclass
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
CORS(app)
app.app_context().push()

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

@app.route('/api/products')
def index():
    return jsonify(Product.query.all())

@app.route("/api/user")
def like():
    req = requests.get("http://host.docker.internal:8000/api/user")
    return jsonify(req.json())

if __name__ == "__main__":
    app.run(debug=True)