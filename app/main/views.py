# -*- coding:utf-8 -*-

from flask import render_template, jsonify, request
from . import main
from .. import db
from ..models import Material, Client, MaterialPrice, Machine, MachinePrice
import json


@main.route('/')
def index():
    return render_template('index.html')

# jqgrid演示例子
@main.route('/simple')
def simple():
    return render_template('simple.html')

@main.route('/simple_getdata')
def simple_getdata():
    return jsonify(json.load(open('app/static/data.json')))


# 设置材料
@main.route('/set_materials')
def set_materials():
    return render_template('set_materials.html')


@main.route('/material_getdata')
def material_getdata():
    materials = []
    for material in Material.query.all():
        materials.append(material.get_dict())
        # print(materials)
        # print(jsonify(materials))
    return jsonify({'rows': materials})


@main.route('/material_add', methods=['POST'])
def material_add():
    name = request.form.get('name')
    if Material.query.filter_by(name=name).first() is not None:
        return jsonify({'result': False, 'message': '此条目已存在'})
    try:
        density = request.form.get('density')
        db.session.add(Material(name=name, density=density))
        db.session.commit()
        material_id = Material.query.filter_by(name=name).first().id
        for client in Client.query.all():
            # print(client.id)
            # print(material_id)
            db.session.add(MaterialPrice(client_id=client.id, material_id=material_id, price=999))
            db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '增加操作执行成功'})


@main.route('/material_delete', methods=['POST'])
def material_delete():
    name = request.form.get('name')
    material = Material.query.filter_by(name=name).first()
    material_id = material.id
    if material is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    try:
        materialprices = MaterialPrice.query.filter_by(material_id=material_id).all()
        for materialprice in materialprices:
            db.session.delete(materialprice)
            db.commit()
        db.session.delete(material)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '增加删除执行成功'})


@main.route('/material_edit', methods=['POST'])
def material_edit():
    old_name = request.form.get('old_name')
    name = request.form.get('name')
    density = request.form.get('density')
    material = Material.query.filter_by(name=old_name).first()
    if material is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    try:
        material.name = name
        material.density = density
        db.session.add(material)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '增加删除执行成功'})


# 设置客户
@main.route('/set_clients')
def set_clients():
    return render_template('set_clients.html')


@main.route('/client_getdata')
def client_getdata():
    clients = []
    for client in Client.query.all():
        clients.append(client.get_dict())
        # print(jsonify(clients))
    return jsonify({'rows': clients})


@main.route('/client_add', methods=['POST'])
def client_add():
    name = request.form.get('name')
    if Client.query.filter_by(name=name).first() is not None:
        return jsonify({'result': False, 'message': '此条目已存在'})
    try:
        db.session.add(Client(name=name))
        db.session.commit()
        client_id = Client.query.filter_by(name=name).first().id
        for material in Material.query.all():
            db.session.add(MaterialPrice(client_id=client_id, material_id=material.id, price=999.9))
        for machine in Machine.query.all():
            db.session.add(MachinePrice(client_id=client_id, machine_id=machine.id, price=999.9))
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '增加操作执行成功'})


@main.route('/client_delete', methods=['POST'])
def client_delete():
    name = request.form.get('name')
    client = Client.query.filter_by(name=name).first()
    if client is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    try:
        client_id = client.id
        for materialprice in MaterialPrice.query.filter_by(client_id=client_id).all():
            db.session.delete(materialprice)
        for machineprice in MachinePrice.query.filter_by(client_id=client_id).all():
            db.session.delete(machineprice)
        db.session.delete(client)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '增加删除执行成功'})


@main.route('/client_edit', methods=['POST'])
def client_edit():
    old_name = request.form.get('old_name')
    name = request.form.get('name')
    client = Client.query.filter_by(name=old_name).first()
    if client is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    try:
        client.name = name
        db.session.add(client)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '客户编辑执行成功'})


# 设置材料价格
@main.route('/set_material_prices')
def set_material_prices():
    clients = []
    for client in Client.query.all():
        clients.append(client.name)
    return render_template('set_material_prices.html', clients=clients)


@main.route('/material_price_getdata')
def material_price_getdata():
    client_name = request.args.get('client')
    client = Client.query.filter_by(name=client_name).first()
    # print(client)
    material_prices = []
    if client is not None:
        for material_price in client.material_prices.all():
            material_prices.append(material_price.get_dict())
            # print(jsonify(clients))
        return jsonify({'rows': material_prices})
    return jsonify({'rows': []})


@main.route('/material_price_edit', methods=['POST'])
def material_price_edit():
    client_name = request.form.get('client_name')
    print(client_name)
    client_id = Client.query.filter_by(name=client_name).first().id
    material_name = request.form.get('material')
    material_id = Material.query.filter_by(name=material_name).first().id
    price = request.form.get('price')
    print(client_id, material_id)
    materialprice = MaterialPrice.query.filter_by(client_id=client_id).filter_by(material_id=material_id).first()
    if materialprice is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    try:
        materialprice.price = price
        db.session.add(materialprice)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '材料价格编辑执行成功'})


# 设置机床
@main.route('/set_machines')
def set_machines():
    return render_template('set_machines.html')

@main.route('/machie_getdata')
def machine_getdata():
    machines = []
    for machine in Machine.query.all():
        machines.append(machine.get_dict())
    return jsonify({'rows': machines})

@main.route('/machine_add', methods=['POST'])
def machine_add():
    name = request.form.get('name')
    key = request.form.get('key')
    if Machine.query.filter_by(name=name).first() is not None:
        return jsonify({'result': False, 'message': '此条目已存在'})
    try:
        db.session.add(Machine(name=name, key=key))
        db.session.commit()
        machine_id = Machine.query.filter_by(name=name).first().id
        for client in Client.query.all():
            db.session.add(MachinePrice(client_id=client.id, machine_id=machine_id, price=999))
            db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '增加操作执行成功'})


@main.route('/machine_delete', methods=['POST'])
def machine_delete():
    name = request.form.get('name')
    machine = Machine.query.filter_by(name=name).first()
    machine_id = machine.id
    print(machine_id)
    if machine is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    try:
        machineprices = MachinePrice.query.filter_by(machine_id=machine_id).all()
        print(machineprices)
        for machineprice in machineprices:
            print(machineprice)   
            db.session.delete(machineprice)
            db.session.commit()
        db.session.delete(machine)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '增加删除执行成功'})


@main.route('/machine_edit', methods=['POST'])
def machine_edit():
    old_name = request.form.get('old_name')
    name = request.form.get('name')
    key = request.form.get('key')
    machine = Machine.query.filter_by(name=old_name).first()
    if machine is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    try:
        machine.name = name
        machine.key = key
        db.session.add(machine)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '客户编辑执行成功'})


# 设置机床收费价格
@main.route('/set_machine_prices')
def set_machine_prices():
    clients = []
    for client in Client.query.all():
        clients.append(client.name)
    return render_template('set_machine_prices.html', clients=clients)


@main.route('/machine_price_getdata')
def machine_price_getdata():
    client_name = request.args.get('client')
    client = Client.query.filter_by(name=client_name).first()
    # print(client)
    machine_prices = []
    if client is not None:
        for machine_price in client.machine_prices.all():
            machine_prices.append(machine_price.get_dict())
            # print(jsonify(clients))
        return jsonify({'rows': machine_prices})
    return jsonify({'rows': []})


@main.route('/machine_price_edit', methods=['POST'])
def machine_price_edit():
    client_name = request.form.get('client_name')
    print(client_name)
    client_id = Client.query.filter_by(name=client_name).first().id
    machine_name = request.form.get('machine')
    machine_id = Machine.query.filter_by(name=machine_name).first().id
    price = request.form.get('price')
    print(client_id, machine_id)
    machineprice = MachinePrice.query.filter_by(client_id=client_id).filter_by(machine_id=machine_id).first()
    if machineprice is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    try:
        machineprice.price = price
        db.session.add(machineprice)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '材料价格编辑执行成功'})

