# -*- coding:utf-8 -*-

from . import db


class Material(db.Model):
    __tablename__ = 'Materials'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    density = db.Column(db.Float)
    prices = db.relationship('MaterialPrice', backref='Material', lazy='dynamic')

    def __repr__(self):
        return "Id: {0} Material {1}: density {2}".format(self.id, self.name, self.density)

    def get_dict(self):
        return {'name': self.name, 'density': self.density}


class Machine(db.Model):
    __tablename__ = 'Machines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    key = db.Column(db.String(1), unique=True)
    prices = db.relationship('MachinePrice', backref='Machine', lazy='dynamic')

    def __repr__(self):
        return "Id: {0} Machine {1} key {2}".format(self.id, self.name, self.key)

    def get_dict(self):
        return {'name': self.name, 'key': self.key}


class Client(db.Model):
    __tablename__ = 'Clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    material_prices = db.relationship('MaterialPrice', backref='Client', lazy='dynamic')
    machine_prices = db.relationship('MachinePrice', backref='Client', lazy='dynamic')

    def __repr__(self):
        return "Id: {0} Client {1}".format(self.id, self.name)

    def get_dict(self):
        return {'name': self.name}


class MaterialPrice(db.Model):
    __tablename__ = 'MaterialPrices'
    id = db.Column(db.Integer, primary_key=True)
    material_id = db.Column(db.Integer, db.ForeignKey('Materials.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('Clients.id'))
    price = db.Column(db.Float)

    def __repr__(self):
        return "material_id: {0} client_id: {1}, price: {2}".format(self.material_id, self.client_id, self.price)

    def get_dict(self):
        return {
        'client': Client.query.filter_by(id=self.client_id).first().name,
        'material': Material.query.filter_by(id=self.material_id).first().name,
        'price': self.price
        }


class MachinePrice(db.Model):
    __tablename__ = 'MachinePrices'
    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('Machines.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('Clients.id'))
    price = db.Column(db.Float)

    def __repr__(self):
        return "machine_id: {0} client_id: {1}, price: {2}".format(self.machine_id, self.client_id, self.price)

    def get_dict(self):
        return {
        'client': Client.query.filter_by(id=self.client_id).first().name,
        'machine': Machine.query.filter_by(id=self.machine_id).first().name,
        'price': self.price
        }


class Measure(db.Model):
    __tablename__ = 'Measures'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return "Id: {0} Measure {1}".format(self.id, self.name)

    def get_dict(self):
        return {'name': self.name}


class PartType(db.Model):
    __tablename__ = 'PartTypes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return "Id: {0} PartType {1}".format(self.id, self.name)

    def get_dict(self):
        return {'name': self.name}


class MaterialShape(db.Model):
    __tablename__ = 'MaterialShapes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return "Id: {0} MaterialShape {1}".format(self.id, self.name)

    def get_dict(self):
        return {'name': self.name}


class Project(db.Model):
    __tablename__ = 'Projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    orders = db.relationship('Order', backref='Project', lazy='dynamic')
    hide = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return "Id: {0} Project {1} hide {2}".format(self.id, self.name, self.hide)

    def get_dict(self):
        return {'name': self.name, 'hide': self.hide}


class Order(db.Model):
    __tablename__ = 'Orders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    client_name = db.Column(db.String(64))
    project_id = db.Column(db.Integer, db.ForeignKey('Projects.id'))
    hide = db.Column(db.Boolean, nullable=False)
    parts = db.relationship('Part', backref='Order', lazy='dynamic')
    price = db.Column(db.Float)


class Part(db.Model):
    __tablename__ = 'Parts'
    order_id = db.Column(db.Integer, db.ForeignKey('Orders.id'))
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    drawing_number = db.Column(db.String(128), unique=True)
    measure = db.Column(db.String(64))
    part_type = db.Column(db.String(64))
    material_type = db.Column(db.String(64))
    material = db.Column(db.String(64))
    number = db.Column(db.Integer)
    size1 = db.Column(db.Float)
    size2 = db.Column(db.Float)
    size3 = db.Column(db.Float)
    weight = db.Column(db.Float)
    commit = db.Column(db.String(256))
    material_price = db.Column(db.Float)
    material_total_price = db.Column(db.Float)
    rude_process1 = db.Column(db.String(64))
    rude_process2 = db.Column(db.String(64))
    rude_process3 = db.Column(db.String(64))
    rude_process4 = db.Column(db.String(64))
    rude_process5 = db.Column(db.String(64))
    rude_process6 = db.Column(db.String(64))
    rude_process7 = db.Column(db.String(64))
    fine_process1 = db.Column(db.String(64))
    fine_process2 = db.Column(db.String(64))
    fine_process3 = db.Column(db.String(64))
    fine_process4 = db.Column(db.String(64))
    fine_process5 = db.Column(db.String(64))
    fine_process6 = db.Column(db.String(64))
    fine_process7 = db.Column(db.String(64))
    fine_process8 = db.Column(db.String(64))

    rude_process1_time = db.Column(db.Float)
    rude_process2_time = db.Column(db.Float)
    rude_process3_time = db.Column(db.Float)
    rude_process4_time = db.Column(db.Float)
    rude_process5_time = db.Column(db.Float)
    rude_process6_time = db.Column(db.Float)
    rude_process7_time = db.Column(db.Float)
    fine_process1_time = db.Column(db.Float)
    fine_process2_time = db.Column(db.Float)
    fine_process3_time = db.Column(db.Float)
    fine_process4_time = db.Column(db.Float)
    fine_process5_time = db.Column(db.Float)
    fine_process6_time = db.Column(db.Float)
    fine_process7_time = db.Column(db.Float)
    fine_process8_time = db.Column(db.Float)

    rude_process1_price = db.Column(db.Float)
    rude_process2_price = db.Column(db.Float)
    rude_process3_price = db.Column(db.Float)
    rude_process4_price = db.Column(db.Float)
    rude_process5_price = db.Column(db.Float)
    rude_process6_price = db.Column(db.Float)
    rude_process7_price = db.Column(db.Float)
    fine_process1_price = db.Column(db.Float)
    fine_process2_price = db.Column(db.Float)
    fine_process3_price = db.Column(db.Float)
    fine_process4_price = db.Column(db.Float)
    fine_process5_price = db.Column(db.Float)
    fine_process6_price = db.Column(db.Float)
    fine_process7_price = db.Column(db.Float)
    fine_process8_price = db.Column(db.Float)

    rude_process1_total_price = db.Column(db.Float)
    rude_process2_total_price = db.Column(db.Float)
    rude_process3_total_price = db.Column(db.Float)
    rude_process4_total_price = db.Column(db.Float)
    rude_process5_total_price = db.Column(db.Float)
    rude_process6_total_price = db.Column(db.Float)
    rude_process7_total_price = db.Column(db.Float)
    fine_process1_total_price = db.Column(db.Float)
    fine_process2_total_price = db.Column(db.Float)
    fine_process3_total_price = db.Column(db.Float)
    fine_process4_total_price = db.Column(db.Float)
    fine_process5_total_price = db.Column(db.Float)
    fine_process6_total_price = db.Column(db.Float)
    fine_process7_total_price = db.Column(db.Float)
    fine_process8_total_price = db.Column(db.Float)

    single_process_price = db.Column(db.Float)
    total_price = db.Column(db.Float)

    def __repr__(self):
        return "Id: {0} name {1} drawing_number {2} number {3}".format(self.id, self.name, self.drawing_number, self.number)

    def get_dict(self):
        return {'id': self.id,'name': self.name, 'drawing_number': self.drawing_number, 'number': self.number, 'total_price': self.total_price}

    def get_detail_dict(self):
        return {
            'name': self.name,
            'drawing_number': self.drawing_number,
            'part_type' : self.part_type,
            'measure': self.measure,
            'material_type': self.material_type,
            'material': self.material,
            'number': self.number,
            'size1': self.size1,
            'size2': self.size2,
            'size3': self.size3,
            'weight': self.weight,
            'commit': self.commit,
            'material_price': self.material_price,
            'material_total_price': self.material_total_price,
            'rude_process1': self.rude_process1,
            'rude_process2': self.rude_process2,
            'rude_process3': self.rude_process3,
            'rude_process4': self.rude_process4,
            'rude_process5': self.rude_process5,
            'rude_process6': self.rude_process6,
            'rude_process7': self.rude_process7,
            'fine_process1': self.fine_process1,
            'fine_process2': self.fine_process2,
            'fine_process3': self.fine_process3,
            'fine_process4': self.fine_process4,
            'fine_process5': self.fine_process5,
            'fine_process6': self.fine_process6,
            'fine_process7': self.fine_process7,
            'fine_process8': self.fine_process8,
            'rude_process1_time': self.rude_process1_time,
            'rude_process2_time': self.rude_process2_time,
            'rude_process3_time': self.rude_process3_time,
            'rude_process4_time': self.rude_process4_time,
            'rude_process5_time': self.rude_process5_time,
            'rude_process6_time': self.rude_process6_time,
            'rude_process7_time': self.rude_process7_time,
            'fine_process1_time': self.fine_process1_time,
            'fine_process2_time': self.fine_process2_time,
            'fine_process3_time': self.fine_process3_time,
            'fine_process4_time': self.fine_process4_time,
            'fine_process5_time': self.fine_process5_time,
            'fine_process6_time': self.fine_process6_time,
            'fine_process7_time': self.fine_process7_time,
            'fine_process8_time': self.fine_process8_time,
            'rude_process1_price': self.rude_process1_price,
            'rude_process2_price': self.rude_process2_price,
            'rude_process3_price': self.rude_process3_price,
            'rude_process4_price': self.rude_process4_price,
            'rude_process5_price': self.rude_process5_price,
            'rude_process6_price': self.rude_process6_price,
            'rude_process7_price': self.rude_process7_price,
            'fine_process1_price': self.fine_process1_price,
            'fine_process2_price': self.fine_process2_price,
            'fine_process3_price': self.fine_process3_price,
            'fine_process4_price': self.fine_process4_price,
            'fine_process5_price': self.fine_process5_price,
            'fine_process6_price': self.fine_process6_price,
            'fine_process7_price': self.fine_process7_price,
            'fine_process8_price': self.fine_process8_price,
            'rude_process1_total_price': self.rude_process1_total_price,
            'rude_process2_total_price': self.rude_process2_total_price,
            'rude_process3_total_price': self.rude_process3_total_price,
            'rude_process4_total_price': self.rude_process4_total_price,
            'rude_process5_total_price': self.rude_process5_total_price,
            'rude_process6_total_price': self.rude_process6_total_price,
            'rude_process7_total_price': self.rude_process7_total_price,
            'fine_process1_total_price': self.fine_process1_total_price,
            'fine_process2_total_price': self.fine_process2_total_price,
            'fine_process3_total_price': self.fine_process3_total_price,
            'fine_process4_total_price': self.fine_process4_total_price,
            'fine_process5_total_price': self.fine_process5_total_price,
            'fine_process6_total_price': self.fine_process6_total_price,
            'fine_process7_total_price': self.fine_process7_total_price,
            'fine_process8_total_price': self.fine_process8_total_price,
            'single_process_price': self.single_process_price,
            'total_price': self.total_price
        }



