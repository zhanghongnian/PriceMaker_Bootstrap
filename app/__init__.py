# -*- coding:utf-8 -*-

from flask import Flask
from config import config
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.bootstrap import Bootstrap

moment = Moment()
db = SQLAlchemy()
# bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    moment.init_app(app)
    db.init_app(app)
    # bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .measure import measure as measure_blueprint
    app.register_blueprint(measure_blueprint)
    from .part_type import part_type as part_type_blueprint
    app.register_blueprint(part_type_blueprint)
    from .material_shape import material_shape as material_shape_blueprint
    app.register_blueprint(material_shape_blueprint)
    from .part import part as part_blueprint
    app.register_blueprint(part_blueprint)
    from .make_order import make_order as make_order_blueprint
    app.register_blueprint(make_order_blueprint)


    return app
