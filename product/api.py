from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_script import Manager

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy()
migrate = Migrate(app, db)


###########################

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:test@database-service:5432/testdb'
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False
## New
app.config['PROPAGATE_EXCEPTIONS'] = True
### ACHTUNG
app.secret_key = 'matthias' # Das sollte nich öffentlich einsehbar sein

############################


class ProductModel(db.Model):
    __tablename = 'product'

    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(80))
    price = db.Column(db.Integer)
    count = db.Column(db.Integer)

    def __init__(self, product, price, count):
        self.product = product
        self.price = price
        self.count = count

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_product(cls, product):
        return cls.query.filter_by(product=product).first()

    def json(self):
        return {'product': self.product, 'price': self.price, 'count': self.count}


class Product(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product', type=str, required=True, help="This field not left blank")
        parser.add_argument('price', type=str, required=True, help="This field not left blank")
        parser.add_argument('count', type=str, required=True, help="This field not left blank")

        data = parser.parse_args()

        if ProductModel.find_by_product(data['product']):
            return {'message': 'Product already exist'}, 400

        product = ProductModel(**data)
        product.save_to_db()

        return product.json(), 200

class ProductList(Resource):
    def get(self):
        return {'products': [product.json() for product in ProductModel.query.all()]}, 200


# @app.before_first_request
# def create_tables():
#     db.create_all()


api.add_resource(ProductList, '/')
api.add_resource(Product, '/add')

if __name__ == '__main__':
    db.init_app(app)
    app.run(host='0.0.0.0', port=80, debug=True)
