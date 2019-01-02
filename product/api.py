from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from db import db
from models.dummy import DummyModel
from resources.dummy import Dummy, DummyList
import config

app = Flask(__name__)
api = Api(app)
migrate = Migrate(app, db)

############################
### LOAD CONFIGRUATION
############################
app.config.from_object(config.DevelopmentConfig)
#app.config.from_object(config.ProductionConfig)

############################
### ADD REST API ENDPOINTS
############################
api.add_resource(DummyList, '/pch/dummy/v1')
api.add_resource(Dummy, '/pch/dummy/v1/add')

if __name__ == '__main__':
    db.init_app(app)
    app.run(host='0.0.0.0', port=80)
