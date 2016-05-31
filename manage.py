# -*- coding:utf-8 -*-

import os
from app import create_app, db
from app.models import Material, Client, MaterialPrice, Machine, \
MachinePrice, Part, Measure, PartType, MaterialShape, Project, Order
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

def make_shell_context():
    return dict(app=app, db=db, Client=Client, 
                Material=Material, MaterialPrice=MaterialPrice, 
                Machine=Machine, MachinePrice=MachinePrice, 
                PartType=PartType, MaterialShape=MaterialShape, Part=Part,
                Project=Project, Order=Order)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
