# -*- coding:utf-8 -*-

from flask import render_template, jsonify, request, current_app, Response, url_for
from . import make_order
from .. import db
from ..models import Material, Client, MaterialPrice, Machine, \
MachinePrice, Part, Measure, PartType, MaterialShape, Project, Order
import json
from ..utils.create_xlsx import make_excel
import os
from urllib.parse import quote

@make_order.route('/add_project', methods=['POST'])
def add_project():
    name = request.form.get('name')
    project = Project.query.filter_by(name=name).first()
    if project is not None:
        return jsonify({'result': False, 'message': '此条目已存在'})
    db.session.add(Project(name=name, hide=False))
    db.session.commit()
    return jsonify({'result': True, 'message': '增加条目成功'})

@make_order.route('/make_xlsx/<int:downloadid>')
def make_xlsx(downloadid):    
    id = downloadid
    order = Order.query.filter_by(id=id).first()
    make_excel(order, current_app.config['EXCEL_DIR'])
    # return jsonify({'result': True, 'message': '生成excel成功'})
    # print(1111)
    # print(os.path.join(current_app.config['EXCEL_DIR'], order.name))
    # print(555)
    with open(os.path.join(current_app.config['EXCEL_DIR'], order.name) + '.xlsx', 'rb') as f:
        rst = Response(f.read(), mimetype='application/octet-stream')
        # print(2222)
        rst.headers['content-disposition'] = 'attachment;filename={0}'.format(quote(order.name+'.xlsx'))
        return rst


@make_order.route('/set_order_client', methods=['POST'])
def set_order_client():
    id = request.form.get('order_id')
    # print(id)
    client = request.form.get('client')
    order = Order.query.filter_by(id=id).first()
    if order is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    order.client_name = client
    db.session.add(order)
    db.session.commit()
    client_id = Client.query.filter_by(name=client).first().id
    for part in order.parts:
        re_clac_price(part, client_id)
    return jsonify({'result': True, 'message': '修改订单客户成功'})


def re_clac_price(part, client_id):
    if part.rude_process1:
        # print(part.rude_process1_price)
        machine1_id = Machine.query.filter_by(name=part.rude_process1).first().id
        part.rude_process1_price = MachinePrice.query.filter_by(client_id=client_id).\
                                filter_by(machine_id=machine1_id).first().price
        part.rude_process1_total_price = part.rude_process1_price * part.rude_process1_time
        # print(part.rude_process1_price)
    if part.rude_process2:
        machine2_id = Machine.query.filter_by(name=part.rude_process2).first().id
        part.rude_process2_price = MachinePrice.query.filter_by(client_id=client_id).\
                                filter_by(machine_id=machine2_id).first().price
        part.rude_process2_total_price = part.rude_process2_price * part.rude_process2_time
    if part.rude_process3:
        machine3_id = Machine.query.filter_by(name=part.rude_process3).first().id
        part.rude_process3_price = MachinePrice.query.filter_by(client_id=client_id).\
                                filter_by(machine_id=machine3_id).first().price
        part.rude_process3_total_price = part.rude_process3_price * part.rude_process3_time
    if part.rude_process4:
        machine4_id = Machine.query.filter_by(name=part.rude_process4).first().id
        part.rude_process4_price = MachinePrice.query.filter_by(client_id=client_id).\
                                filter_by(machine_id=machine4_id).first().price
        part.rude_process4_total_price = part.rude_process4_price * part.rude_process4_time
    if part.rude_process5:
        machine5_id = Machine.query.filter_by(name=part.rude_process5).first().id
        part.rude_process5_price = MachinePrice.query.filter_by(client_id=client_id).\
                                filter_by(machine_id=machine5_id).first().price
        part.rude_process5_total_price = part.rude_process5_price * part.rude_process5_time
    if part.rude_process6:
        machine6_id = Machine.query.filter_by(name=part.rude_process6).first().id
        part.rude_process6_price = MachinePrice.query.filter_by(client_id=client_id).\
                                filter_by(machine_id=machine6_id).first().price
        part.rude_process6_total_price = part.rude_process6_price * part.rude_process6_time
    if part.rude_process7:
        machine7_id = Machine.query.filter_by(name=part.rude_process7).first().id
        part.rude_process7_price = MachinePrice.query.filter_by(client_id=client_id).\
                                filter_by(machine_id=machine7_id).first().price
        part.rude_process7_total_price = part.rude_process7_price * part.rude_process7_time
    if part.fine_process1:
        # print(part.fine_process1_price)
        machine1_id = Machine.query.filter_by(name=part.fine_process1).first().id
        part.fine_process1_price = MachinePrice.query.filter_by(client_id=client_id).\
                                filter_by(machine_id=machine1_id).first().price
        part.fine_process1_total_price = part.fine_process1_price * part.fine_process1_time
        # print(part.fine_process1_price)
    if part.fine_process2:
        machine2_id = Machine.query.filter_by(name=part.fine_process2).first().id
        part.fine_process2_price = MachinePrice.query.filter_by(client_id=client_id).\
                                filter_by(machine_id=machine2_id).first().price
        part.fine_process2_total_price = part.fine_process2_price * part.fine_process2_time
    if part.fine_process3:
        machine3_id = Machine.query.filter_by(name=part.fine_process3).first().id
        part.fine_process3_price = MachinePrice.query.filter_by(client_id=client_id).\
                                filter_by(machine_id=machine3_id).first().price
        part.fine_process3_total_price = part.fine_process3_price * part.fine_process3_time
    if part.fine_process4:
        machine4_id = Machine.query.filter_by(name=part.fine_process4).first().id
        part.fine_process4_price = MachinePrice.query.filter_by(client_id=client_id).\
                                filter_by(machine_id=machine4_id).first().price
        part.fine_process4_total_price = part.fine_process4_price * part.fine_process4_time
    if part.fine_process5:
        machine5_id = Machine.query.filter_by(name=part.fine_process5).first().id
        part.fine_process5_price = MachinePrice.query.filter_by(client_id=client_id).\
                                filter_by(machine_id=machine5_id).first().price
        part.fine_process5_total_price = part.fine_process5_price * part.fine_process5_time
    if part.fine_process6:
        machine6_id = Machine.query.filter_by(name=part.fine_process6).first().id
        part.fine_process6_price = MachinePrice.query.filter_by(client_id=client_id).\
                                filter_by(machine_id=machine6_id).first().price
        part.fine_process6_total_price = part.fine_process6_price * part.fine_process6_time
    if part.fine_process7:
        machine7_id = Machine.query.filter_by(name=part.fine_process7).first().id
        part.fine_process7_price = MachinePrice.query.filter_by(client_id=client_id).\
                                filter_by(machine_id=machine7_id).first().price
        part.fine_process7_total_price = part.fine_process7_price * part.fine_process7_time
    if part.fine_process8:
        machine8_id = Machine.query.filter_by(name=part.fine_process8).first().id
        part.fine_process8_price = MachinePrice.query.filter_by(client_id=client_id).\
                                filter_by(machine_id=machine8_id).first().price
        part.fine_process8_total_price = part.fine_process8_price * part.fine_process8_time
    part.single_process_price = part.rude_process1_total_price + part.rude_process2_total_price + part.rude_process3_total_price + \
                                part.rude_process4_total_price + part.rude_process5_total_price + part.rude_process6_total_price + \
                                part.rude_process7_total_price + \
                                part.fine_process1_total_price + part.fine_process2_total_price + part.fine_process3_total_price + \
                                part.fine_process4_total_price + part.fine_process5_total_price + part.fine_process6_total_price + \
                                part.fine_process7_total_price + part.fine_process8_total_price
    if part.material:
        material_id = Material.query.filter_by(name=part.material).first().id
        part.material_price = MaterialPrice.query.filter_by(client_id=client_id).\
                            filter_by(material_id=material_id).first().price
    part.material_total_price = part.material_price * part.weight
    part.total_price = (part.single_process_price + part.material_total_price) * part.number
    db.session.add(part)
    db.session.commit()


@make_order.route('/add_order', methods=['POST'])
def add_order():
    project_name = request.form.get('project')
    name = request.form.get('name')
    order = Order.query.filter_by(name=name).first()
    project = Project.query.filter_by(name=name).first()
    if project is not None:
        return jsonify({'result': False, 'message': '订单名不能与项目名相同'})
    project = Project.query.filter_by(name=project_name).first()
    if project is None:
        return jsonify({'result': False, 'message': '此项目已不存在'})
    # order = project.orders.filter_by(hide=False).filter_by(name=name).first()
    order = Order.query.filter_by(hide=False).filter_by(name=name).first()
    if order is not None:
        return jsonify({'result': False, 'message': '已有此订单名称'})
    db.session.add(Order(name=name, project_id=project.id, client_name=Client.query.first().name, hide=False))
    db.session.commit()
    return jsonify({'result': True, 'message': '增加条目成功'})


@make_order.route('/remove_project', methods=['POST'])
def remove_project():
    name = request.form.get('name')
    project = Project.query.filter_by(name=name).first()
    if project is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    project.hide = True
    # db.session.delete(project)
    db.session.add(project)
    db.session.commit()
    return jsonify({'result': True, 'message': '删除条目成功'})

@make_order.route('/project_exist', methods=['POST'])
def project_exist():
    name = request.form.get('name')
    project = Project.query.filter_by(hide=False).filter_by(name=name).first()
    if project is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    return jsonify({'result': True, 'message': '此条目存在'})

@make_order.route('/order_exist', methods=['POST'])
def order_exist():
    name = request.form.get('name')
    order = Order.query.filter_by(hide=False).filter_by(name=name).first()
    if order is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    return jsonify({'result': True, 'message': '此条目存在', 'result_id': order.id,
     'client_name': order.client_name, 'downloadlink': url_for('make_order.make_xlsx', downloadid=order.id)})


@make_order.route('/remove_order', methods=['POST'])
def remove_order():
    name = request.form.get('name')
    order = Order.query.filter_by(name=name).first()
    if order is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    order.hide = True
    db.session.add(order)
    # db.session.delete(order)
    db.session.commit()
    return jsonify({'result': True, 'message': '删除条目成功'})


@make_order.route('/get_project_tree', methods=['POST'])
def get_project_tree():
    projects = []
    for project in Project.query.filter_by(hide=False).all():
        orders = []
        for order in Order.query.filter_by(hide=False).filter_by(project_id=project.id).all():
            orders.append({'text': order.name})
        if len(orders) > 0:
            projects.append({'text': project.name, 'nodes': orders})
        else:
            projects.append({'text': project.name})
    return jsonify({'tree': projects})


# 设置客户
@make_order.route('/set_order')
def set_order():
    clients = []
    for client in Client.query.all():
        clients.append(client.name)
    measures = []
    for measure in Measure.query.all():
        measures.append(measure.name)
    part_types = []
    for part_type in PartType.query.all():
        part_types.append(part_type.name)
    material_shapes = []
    for material_shape in MaterialShape.query.all():
        material_shapes.append(material_shape.name)
    materials = []
    for material in Material.query.all():
        materials.append(material.name)
        # print(material.name)
    machines = []
    for machine in Machine.query.all():
        machines.append(machine.name)
        # print(machine.name)
    machine_key_dict = {}
    for machine in Machine.query.all():
        machine_key_dict[machine.name] = machine.key
    return render_template('set_order.html', 
        measures=measures, part_types=part_types,
        material_shapes=material_shapes, materials=materials,
        machines=machines, clients=clients, machine_key_dict=machine_key_dict)


@make_order.route('/part_getdata')
def part_getdata():
    order_id = request.args.get('order_id')
    # print(order_id)

    parts = []
    order_price = 0
    order = Order.query.filter_by(id=order_id).first()
    if order is not None:
        for part in Order.query.filter_by(id=order_id).first().parts:
            parts.append(part.get_dict())
            order_price = order_price + part.total_price
            # print(part.get_dict())
        order.price = order_price
        db.session.add(order)
        db.session.commit()
    return jsonify({'rows': parts, "userdata":{"number": "核价总计","total_price": order_price}})


@make_order.route('/part_get_detail_data', methods=['POST'])
def part_get_detail_data():
    name = request.form.get('modify_name')
    part = Part.query.filter_by(name=name).first()
    if part is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    return jsonify(part.get_detail_dict())



@make_order.route('/submit_part', methods=['POST'])
def submit_part():
    order_id = request.form.get('order_id')
    name = request.form.get('name')
    drawing_number = request.form.get('drawing_number')
    number = request.form.get('number')
    number = number if number else 0
    size1 = request.form.get('size1')
    size1 = size1 if size1 else 0
    size2 = request.form.get('size2')
    size2 = size2 if size2 else 0
    size3 = request.form.get('size3') 
    size3 = size3 if size3 else 0
    commit_textarea = request.form.get('commit_textarea')
    rude_process1_time_input = request.form.get('rude_process1_time_input')
    rude_process1_time_input = rude_process1_time_input if rude_process1_time_input else 0
    rude_process2_time_input = request.form.get('rude_process2_time_input')
    rude_process2_time_input = rude_process2_time_input if rude_process2_time_input else 0
    rude_process3_time_input = request.form.get('rude_process3_time_input')
    rude_process3_time_input = rude_process3_time_input if rude_process3_time_input else 0
    rude_process4_time_input = request.form.get('rude_process4_time_input')
    rude_process4_time_input = rude_process4_time_input if rude_process4_time_input else 0
    rude_process5_time_input = request.form.get('rude_process5_time_input')
    rude_process5_time_input = rude_process5_time_input if rude_process5_time_input else 0
    rude_process6_time_input = request.form.get('rude_process6_time_input')
    rude_process6_time_input = rude_process6_time_input if rude_process6_time_input else 0
    rude_process7_time_input = request.form.get('rude_process7_time_input')
    rude_process7_time_input = rude_process7_time_input if rude_process7_time_input else 0
    fine_process1_time_input = request.form.get('fine_process1_time_input')
    fine_process1_time_input = fine_process1_time_input if fine_process1_time_input else 0
    fine_process2_time_input = request.form.get('fine_process2_time_input')
    fine_process2_time_input = fine_process2_time_input if fine_process2_time_input else 0
    fine_process3_time_input = request.form.get('fine_process3_time_input')
    fine_process3_time_input = fine_process3_time_input if fine_process3_time_input else 0
    fine_process4_time_input = request.form.get('fine_process4_time_input')
    fine_process4_time_input = fine_process4_time_input if fine_process4_time_input else 0
    fine_process5_time_input = request.form.get('fine_process5_time_input')
    fine_process5_time_input = fine_process5_time_input if fine_process5_time_input else 0
    fine_process6_time_input = request.form.get('fine_process6_time_input')
    fine_process6_time_input = fine_process6_time_input if fine_process6_time_input else 0
    fine_process7_time_input = request.form.get('fine_process7_time_input')
    fine_process7_time_input = fine_process7_time_input if fine_process7_time_input else 0
    fine_process8_time_input = request.form.get('fine_process8_time_input')
    fine_process8_time_input = fine_process8_time_input if fine_process8_time_input else 0
    material_select = request.form.get('material_select')
    measure_select = request.form.get('measure_select')
    part_type_select = request.form.get('part_type_select')
    material_shape_select = request.form.get('material_shape_select')
    rude_process1_select = request.form.get('rude_process1_select')
    rude_process2_select = request.form.get('rude_process2_select')
    rude_process3_select = request.form.get('rude_process3_select')
    rude_process4_select = request.form.get('rude_process4_select')
    rude_process5_select = request.form.get('rude_process5_select')
    rude_process6_select = request.form.get('rude_process6_select')
    rude_process7_select = request.form.get('rude_process7_select')
    fine_process1_select = request.form.get('fine_process1_select')
    fine_process2_select = request.form.get('fine_process2_select')
    fine_process3_select = request.form.get('fine_process3_select')
    fine_process4_select = request.form.get('fine_process4_select')
    fine_process5_select = request.form.get('fine_process5_select')
    fine_process6_select = request.form.get('fine_process6_select')
    fine_process7_select = request.form.get('fine_process7_select')
    fine_process8_select = request.form.get('fine_process8_select')
    material_weight = request.form.get('material_weight')
    material_weight = material_weight if material_weight else 0
    material_price = request.form.get('material_price')
    material_price = material_price if material_price else 0
    material_totoal_price = request.form.get('material_totoal_price')
    material_totoal_price = material_totoal_price if material_totoal_price else 0
    one_part_process_price = request.form.get('one_part_process_price')
    one_part_process_price = one_part_process_price if one_part_process_price else 0
    total_price = request.form.get('total_price')
    total_price = total_price if total_price else 0
    rude_process1_price_td = request.form.get('rude_process1_price_td')
    rude_process1_price_td = rude_process1_price_td if rude_process1_price_td else 0
    rude_process2_price_td = request.form.get('rude_process2_price_td')
    rude_process2_price_td = rude_process2_price_td if rude_process2_price_td else 0
    rude_process3_price_td = request.form.get('rude_process3_price_td')
    rude_process3_price_td = rude_process3_price_td if rude_process3_price_td else 0
    rude_process4_price_td = request.form.get('rude_process4_price_td')
    rude_process4_price_td = rude_process4_price_td if rude_process4_price_td else 0
    rude_process5_price_td = request.form.get('rude_process5_price_td')
    rude_process5_price_td = rude_process5_price_td if rude_process5_price_td else 0
    rude_process6_price_td = request.form.get('rude_process6_price_td')
    rude_process6_price_td = rude_process6_price_td if rude_process6_price_td else 0
    rude_process7_price_td = request.form.get('rude_process7_price_td')
    rude_process7_price_td = rude_process7_price_td if rude_process7_price_td else 0
    fine_process1_price_td = request.form.get('fine_process1_price_td')
    fine_process1_price_td = fine_process1_price_td if fine_process1_price_td else 0
    fine_process2_price_td = request.form.get('fine_process2_price_td')
    fine_process2_price_td = fine_process2_price_td if fine_process2_price_td else 0
    fine_process3_price_td = request.form.get('fine_process3_price_td')
    fine_process3_price_td = fine_process3_price_td if fine_process3_price_td else 0
    fine_process4_price_td = request.form.get('fine_process4_price_td')
    fine_process4_price_td = fine_process4_price_td if fine_process4_price_td else 0
    fine_process5_price_td = request.form.get('fine_process5_price_td')
    fine_process5_price_td = fine_process5_price_td if fine_process5_price_td else 0
    fine_process6_price_td = request.form.get('fine_process6_price_td')
    fine_process6_price_td = fine_process6_price_td if fine_process6_price_td else 0
    fine_process7_price_td = request.form.get('fine_process7_price_td')
    fine_process7_price_td = fine_process7_price_td if fine_process7_price_td else 0
    fine_process8_price_td = request.form.get('fine_process8_price_td')
    fine_process8_price_td = fine_process8_price_td if fine_process8_price_td else 0
    rude_process1_total_price_td = request.form.get('rude_process1_total_price_td')
    rude_process1_total_price_td = rude_process1_total_price_td if rude_process1_total_price_td else 0
    rude_process2_total_price_td = request.form.get('rude_process2_total_price_td')
    rude_process2_total_price_td = rude_process2_total_price_td if rude_process2_total_price_td else 0
    rude_process3_total_price_td = request.form.get('rude_process3_total_price_td')
    rude_process3_total_price_td = rude_process3_total_price_td if rude_process3_total_price_td else 0
    rude_process4_total_price_td = request.form.get('rude_process4_total_price_td')
    rude_process4_total_price_td = rude_process4_total_price_td if rude_process4_total_price_td else 0
    rude_process5_total_price_td = request.form.get('rude_process5_total_price_td')
    rude_process5_total_price_td = rude_process5_total_price_td if rude_process5_total_price_td else 0
    rude_process6_total_price_td = request.form.get('rude_process6_total_price_td')
    rude_process6_total_price_td = rude_process6_total_price_td if rude_process6_total_price_td else 0
    rude_process7_total_price_td = request.form.get('rude_process7_total_price_td')
    rude_process7_total_price_td = rude_process7_total_price_td if rude_process7_total_price_td else 0
    fine_process1_total_price_td = request.form.get('fine_process1_total_price_td')
    fine_process1_total_price_td = fine_process1_total_price_td if fine_process1_total_price_td else 0
    fine_process2_total_price_td = request.form.get('fine_process2_total_price_td')
    fine_process2_total_price_td = fine_process2_total_price_td if fine_process2_total_price_td else 0
    fine_process3_total_price_td = request.form.get('fine_process3_total_price_td')
    fine_process3_total_price_td = fine_process3_total_price_td if fine_process3_total_price_td else 0
    fine_process4_total_price_td = request.form.get('fine_process4_total_price_td')
    fine_process4_total_price_td = fine_process4_total_price_td if fine_process4_total_price_td else 0
    fine_process5_total_price_td = request.form.get('fine_process5_total_price_td')
    fine_process5_total_price_td = fine_process5_total_price_td if fine_process5_total_price_td else 0
    fine_process6_total_price_td = request.form.get('fine_process6_total_price_td')
    fine_process6_total_price_td = fine_process6_total_price_td if fine_process6_total_price_td else 0
    fine_process7_total_price_td = request.form.get('fine_process7_total_price_td')
    fine_process7_total_price_td = fine_process7_total_price_td if fine_process7_total_price_td else 0
    fine_process8_total_price_td = request.form.get('fine_process8_total_price_td')
    fine_process8_total_price_td = fine_process8_total_price_td if fine_process8_total_price_td else 0

    if Part.query.filter_by(name=name).first() is not None:
        return jsonify({'result': False, 'message': '此条目已存在'})
    try:
        # print(order_id)
        db.session.add(Part(order_id=order_id, name=name, drawing_number=drawing_number,
            measure=measure_select, material_type=material_shape_select,
            material=material_select, number=int(number), part_type=part_type_select,
            size1=float(size1), size2=float(size2), size3=float(size3),
            weight=float(material_weight), commit=commit_textarea,
            material_price=float(material_price), material_total_price=float(material_totoal_price),
            rude_process1=rude_process1_select,
            rude_process2=rude_process2_select,
            rude_process3=rude_process3_select,
            rude_process4=rude_process4_select,
            rude_process5=rude_process5_select,
            rude_process6=rude_process6_select,
            rude_process7=rude_process7_select,
            rude_process1_time=float(rude_process1_time_input),
            rude_process2_time=float(rude_process2_time_input),
            rude_process3_time=float(rude_process3_time_input),
            rude_process4_time=float(rude_process4_time_input),
            rude_process5_time=float(rude_process5_time_input),
            rude_process6_time=float(rude_process6_time_input),
            rude_process7_time=float(rude_process7_time_input),
            fine_process1=fine_process1_select,
            fine_process2=fine_process2_select,
            fine_process3=fine_process3_select,
            fine_process4=fine_process4_select,
            fine_process5=fine_process5_select,
            fine_process6=fine_process6_select,
            fine_process7=fine_process7_select,
            fine_process1_time=float(fine_process1_time_input),
            fine_process2_time=float(fine_process2_time_input),
            fine_process3_time=float(fine_process3_time_input),
            fine_process4_time=float(fine_process4_time_input),
            fine_process5_time=float(fine_process5_time_input),
            fine_process6_time=float(fine_process6_time_input),
            fine_process7_time=float(fine_process7_time_input),
            fine_process8_time=float(fine_process8_time_input),
            rude_process1_price=float(rude_process1_price_td),
            rude_process2_price=float(rude_process2_price_td),
            rude_process3_price=float(rude_process3_price_td),
            rude_process4_price=float(rude_process4_price_td),
            rude_process5_price=float(rude_process5_price_td),
            rude_process6_price=float(rude_process6_price_td),
            rude_process7_price=float(rude_process7_price_td),
            fine_process1_price=float(fine_process1_price_td),
            fine_process2_price=float(fine_process2_price_td),
            fine_process3_price=float(fine_process3_price_td),
            fine_process4_price=float(fine_process4_price_td),
            fine_process5_price=float(fine_process5_price_td),
            fine_process6_price=float(fine_process6_price_td),
            fine_process7_price=float(fine_process7_price_td),
            fine_process8_price=float(fine_process8_price_td),
            rude_process1_total_price=float(rude_process1_total_price_td),
            rude_process2_total_price=float(rude_process2_total_price_td),
            rude_process3_total_price=float(rude_process3_total_price_td),
            rude_process4_total_price=float(rude_process4_total_price_td),
            rude_process5_total_price=float(rude_process5_total_price_td),
            rude_process6_total_price=float(rude_process6_total_price_td),
            rude_process7_total_price=float(rude_process7_total_price_td),
            fine_process1_total_price=float(fine_process1_total_price_td),
            fine_process2_total_price=float(fine_process2_total_price_td),
            fine_process3_total_price=float(fine_process3_total_price_td),
            fine_process4_total_price=float(fine_process4_total_price_td),
            fine_process5_total_price=float(fine_process5_total_price_td),
            fine_process6_total_price=float(fine_process6_total_price_td),
            fine_process7_total_price=float(fine_process7_total_price_td),
            fine_process8_total_price=float(fine_process8_total_price_td),
            single_process_price=float(one_part_process_price),
            total_price=float(total_price)))
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '增加操作执行成功'})


@make_order.route('/part_delete', methods=['POST'])
def part_delete():
    name = request.form.get('name')
    part = Part.query.filter_by(name=name).first()
    if part is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    try:
        db.session.delete(part)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '增加删除执行成功'})


@make_order.route('/modify_part', methods=['POST'])
def modify_part():
    name = request.form.get('name')
    # print(request.form)
    drawing_number = request.form.get('drawing_number')
    number = request.form.get('number')
    part_type = request.form.get('part_type_select')
    # print(part_type)
    number = number if number else 0
    size1 = request.form.get('size1')
    size1 = size1 if size1 else 0
    size2 = request.form.get('size2')
    size2 = size2 if size2 else 0
    size3 = request.form.get('size3') 
    size3 = size3 if size3 else 0
    commit_textarea = request.form.get('commit_textarea')
    rude_process1_time_input = request.form.get('rude_process1_time_input')
    rude_process1_time_input = rude_process1_time_input if rude_process1_time_input else 0
    rude_process2_time_input = request.form.get('rude_process2_time_input')
    rude_process2_time_input = rude_process2_time_input if rude_process2_time_input else 0
    rude_process3_time_input = request.form.get('rude_process3_time_input')
    rude_process3_time_input = rude_process3_time_input if rude_process3_time_input else 0
    rude_process4_time_input = request.form.get('rude_process4_time_input')
    rude_process4_time_input = rude_process4_time_input if rude_process4_time_input else 0
    rude_process5_time_input = request.form.get('rude_process5_time_input')
    rude_process5_time_input = rude_process5_time_input if rude_process5_time_input else 0
    rude_process6_time_input = request.form.get('rude_process6_time_input')
    rude_process6_time_input = rude_process6_time_input if rude_process6_time_input else 0
    rude_process7_time_input = request.form.get('rude_process7_time_input')
    rude_process7_time_input = rude_process7_time_input if rude_process7_time_input else 0
    fine_process1_time_input = request.form.get('fine_process1_time_input')
    fine_process1_time_input = fine_process1_time_input if fine_process1_time_input else 0
    fine_process2_time_input = request.form.get('fine_process2_time_input')
    fine_process2_time_input = fine_process2_time_input if fine_process2_time_input else 0
    fine_process3_time_input = request.form.get('fine_process3_time_input')
    fine_process3_time_input = fine_process3_time_input if fine_process3_time_input else 0
    fine_process4_time_input = request.form.get('fine_process4_time_input')
    fine_process4_time_input = fine_process4_time_input if fine_process4_time_input else 0
    fine_process5_time_input = request.form.get('fine_process5_time_input')
    fine_process5_time_input = fine_process5_time_input if fine_process5_time_input else 0
    fine_process6_time_input = request.form.get('fine_process6_time_input')
    fine_process6_time_input = fine_process6_time_input if fine_process6_time_input else 0
    fine_process7_time_input = request.form.get('fine_process7_time_input')
    fine_process7_time_input = fine_process7_time_input if fine_process7_time_input else 0
    fine_process8_time_input = request.form.get('fine_process8_time_input')
    fine_process8_time_input = fine_process8_time_input if fine_process8_time_input else 0
    material_select = request.form.get('material_select')
    measure_select = request.form.get('measure_select')
    part_type_select = request.form.get('part_type_select')
    material_shape_select = request.form.get('material_shape_select')
    rude_process1_select = request.form.get('rude_process1_select')
    rude_process2_select = request.form.get('rude_process2_select')
    rude_process3_select = request.form.get('rude_process3_select')
    rude_process4_select = request.form.get('rude_process4_select')
    rude_process5_select = request.form.get('rude_process5_select')
    rude_process6_select = request.form.get('rude_process6_select')
    rude_process7_select = request.form.get('rude_process7_select')
    fine_process1_select = request.form.get('fine_process1_select')
    fine_process2_select = request.form.get('fine_process2_select')
    fine_process3_select = request.form.get('fine_process3_select')
    fine_process4_select = request.form.get('fine_process4_select')
    fine_process5_select = request.form.get('fine_process5_select')
    fine_process6_select = request.form.get('fine_process6_select')
    fine_process7_select = request.form.get('fine_process7_select')
    fine_process8_select = request.form.get('fine_process8_select')
    material_weight = request.form.get('material_weight')
    material_weight = material_weight if material_weight else 0
    material_price = request.form.get('material_price')
    material_price = material_price if material_price else 0
    material_totoal_price = request.form.get('material_totoal_price')
    material_totoal_price = material_totoal_price if material_totoal_price else 0
    one_part_process_price = request.form.get('one_part_process_price')
    one_part_process_price = one_part_process_price if one_part_process_price else 0
    total_price = request.form.get('total_price')
    total_price = total_price if total_price else 0
    rude_process1_price_td = request.form.get('rude_process1_price_td')
    # print(rude_process1_price_td)
    rude_process1_price_td = rude_process1_price_td if rude_process1_price_td else 0
    # print(rude_process1_price_td)
    rude_process2_price_td = request.form.get('rude_process2_price_td')
    rude_process2_price_td = rude_process2_price_td if rude_process2_price_td else 0
    rude_process3_price_td = request.form.get('rude_process3_price_td')
    rude_process3_price_td = rude_process3_price_td if rude_process3_price_td else 0
    rude_process4_price_td = request.form.get('rude_process4_price_td')
    rude_process4_price_td = rude_process4_price_td if rude_process4_price_td else 0
    rude_process5_price_td = request.form.get('rude_process5_price_td')
    rude_process5_price_td = rude_process5_price_td if rude_process5_price_td else 0
    rude_process6_price_td = request.form.get('rude_process6_price_td')
    rude_process6_price_td = rude_process6_price_td if rude_process6_price_td else 0
    rude_process7_price_td = request.form.get('rude_process7_price_td')
    rude_process7_price_td = rude_process7_price_td if rude_process7_price_td else 0
    fine_process1_price_td = request.form.get('fine_process1_price_td')
    fine_process1_price_td = fine_process1_price_td if fine_process1_price_td else 0
    fine_process2_price_td = request.form.get('fine_process2_price_td')
    fine_process2_price_td = fine_process2_price_td if fine_process2_price_td else 0
    fine_process3_price_td = request.form.get('fine_process3_price_td')
    fine_process3_price_td = fine_process3_price_td if fine_process3_price_td else 0
    fine_process4_price_td = request.form.get('fine_process4_price_td')
    fine_process4_price_td = fine_process4_price_td if fine_process4_price_td else 0
    fine_process5_price_td = request.form.get('fine_process5_price_td')
    fine_process5_price_td = fine_process5_price_td if fine_process5_price_td else 0
    fine_process6_price_td = request.form.get('fine_process6_price_td')
    fine_process6_price_td = fine_process6_price_td if fine_process6_price_td else 0
    fine_process7_price_td = request.form.get('fine_process7_price_td')
    fine_process7_price_td = fine_process7_price_td if fine_process7_price_td else 0
    fine_process8_price_td = request.form.get('fine_process8_price_td')
    fine_process8_price_td = fine_process8_price_td if fine_process8_price_td else 0
    rude_process1_total_price_td = request.form.get('rude_process1_total_price_td')
    rude_process1_total_price_td = rude_process1_total_price_td if rude_process1_total_price_td else 0
    rude_process2_total_price_td = request.form.get('rude_process2_total_price_td')
    rude_process2_total_price_td = rude_process2_total_price_td if rude_process2_total_price_td else 0
    rude_process3_total_price_td = request.form.get('rude_process3_total_price_td')
    rude_process3_total_price_td = rude_process3_total_price_td if rude_process3_total_price_td else 0
    rude_process4_total_price_td = request.form.get('rude_process4_total_price_td')
    rude_process4_total_price_td = rude_process4_total_price_td if rude_process4_total_price_td else 0
    rude_process5_total_price_td = request.form.get('rude_process5_total_price_td')
    rude_process5_total_price_td = rude_process5_total_price_td if rude_process5_total_price_td else 0
    rude_process6_total_price_td = request.form.get('rude_process6_total_price_td')
    rude_process6_total_price_td = rude_process6_total_price_td if rude_process6_total_price_td else 0
    rude_process7_total_price_td = request.form.get('rude_process7_total_price_td')
    rude_process7_total_price_td = rude_process7_total_price_td if rude_process7_total_price_td else 0
    fine_process1_total_price_td = request.form.get('fine_process1_total_price_td')
    fine_process1_total_price_td = fine_process1_total_price_td if fine_process1_total_price_td else 0
    fine_process2_total_price_td = request.form.get('fine_process2_total_price_td')
    fine_process2_total_price_td = fine_process2_total_price_td if fine_process2_total_price_td else 0
    fine_process3_total_price_td = request.form.get('fine_process3_total_price_td')
    fine_process3_total_price_td = fine_process3_total_price_td if fine_process3_total_price_td else 0
    fine_process4_total_price_td = request.form.get('fine_process4_total_price_td')
    fine_process4_total_price_td = fine_process4_total_price_td if fine_process4_total_price_td else 0
    fine_process5_total_price_td = request.form.get('fine_process5_total_price_td')
    fine_process5_total_price_td = fine_process5_total_price_td if fine_process5_total_price_td else 0
    fine_process6_total_price_td = request.form.get('fine_process6_total_price_td')
    fine_process6_total_price_td = fine_process6_total_price_td if fine_process6_total_price_td else 0
    fine_process7_total_price_td = request.form.get('fine_process7_total_price_td')
    fine_process7_total_price_td = fine_process7_total_price_td if fine_process7_total_price_td else 0
    fine_process8_total_price_td = request.form.get('fine_process8_total_price_td')
    fine_process8_total_price_td = fine_process8_total_price_td if fine_process8_total_price_td else 0

    old_name = request.form.get('old_name')
    # name = request.form.get('name')
    part = Part.query.filter_by(name=old_name).first()
    part_new_name = Part.query.filter_by(name=name).first()
    if part is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    if name != old_name and part_new_name is not None:
        return jsonify({'result': False, 'message': '新名字以存在'})
    try:
        part.name = name
        part.drawing_number=drawing_number
        part.measure=measure_select 
        part.part_type=part_type
        # print(part_type)
        part.material_type=material_shape_select
        part.material=material_select
        part.number=int(number)
        part.size1=float(size1) 
        part.size2=float(size2)
        part.size3=float(size3)
        # print("'" + material_weight + "'")
        part.weight=float(material_weight)
        # print(commit_textarea)
        part.commit=commit_textarea
        part.material_price=float(material_price)
        part.material_total_price=float(material_totoal_price)
        part.rude_process1=rude_process1_select
        part.rude_process2=rude_process2_select
        part.rude_process3=rude_process3_select
        part.rude_process4=rude_process4_select
        part.rude_process5=rude_process5_select
        part.rude_process6=rude_process6_select
        part.rude_process7=rude_process7_select
        part.rude_process1_time=float(rude_process1_time_input)
        part.rude_process2_time=float(rude_process2_time_input)
        part.rude_process3_time=float(rude_process3_time_input)
        part.rude_process4_time=float(rude_process4_time_input)
        part.rude_process5_time=float(rude_process5_time_input)
        part.rude_process6_time=float(rude_process6_time_input)
        part.rude_process7_time=float(rude_process7_time_input)
        part.rude_process1_price=float(rude_process1_price_td)
        part.rude_process2_price=float(rude_process2_price_td)
        part.rude_process3_price=float(rude_process3_price_td)
        part.rude_process4_price=float(rude_process4_price_td)
        part.rude_process5_price=float(rude_process5_price_td)
        part.rude_process6_price=float(rude_process6_price_td)
        part.rude_process7_price=float(rude_process7_price_td)
        part.fine_process1_price=float(fine_process1_price_td)
        part.fine_process2_price=float(fine_process2_price_td)
        part.fine_process3_price=float(fine_process3_price_td)
        part.fine_process4_price=float(fine_process4_price_td)
        part.fine_process5_price=float(fine_process5_price_td)
        part.fine_process6_price=float(fine_process6_price_td)
        part.fine_process7_price=float(fine_process7_price_td)
        part.fine_process8_price=float(fine_process8_price_td)
        part.fine_process1=fine_process1_select
        part.fine_process2=fine_process2_select
        part.fine_process3=fine_process3_select
        part.fine_process4=fine_process4_select
        part.fine_process5=fine_process5_select
        part.fine_process6=fine_process6_select
        part.fine_process7=fine_process7_select
        part.fine_process1_time=float(fine_process1_time_input)
        part.fine_process2_time=float(fine_process2_time_input)
        part.fine_process3_time=float(fine_process3_time_input)
        part.fine_process4_time=float(fine_process4_time_input)
        part.fine_process5_time=float(fine_process5_time_input)
        part.fine_process6_time=float(fine_process6_time_input)
        part.fine_process7_time=float(fine_process7_time_input)
        part.fine_process8_time=float(fine_process8_time_input)
        part.rude_process1_total_price=float(rude_process1_total_price_td)
        part.rude_process2_total_price=float(rude_process2_total_price_td)
        part.rude_process3_total_price=float(rude_process3_total_price_td)
        part.rude_process4_total_price=float(rude_process4_total_price_td)
        part.rude_process5_total_price=float(rude_process5_total_price_td)
        part.rude_process6_total_price=float(rude_process6_total_price_td)
        part.rude_process7_total_price=float(rude_process7_total_price_td)
        part.fine_process1_total_price=float(fine_process1_total_price_td)
        part.fine_process2_total_price=float(fine_process2_total_price_td)
        part.fine_process3_total_price=float(fine_process3_total_price_td)
        part.fine_process4_total_price=float(fine_process4_total_price_td)
        part.fine_process5_total_price=float(fine_process5_total_price_td)
        part.fine_process6_total_price=float(fine_process6_total_price_td)
        part.fine_process7_total_price=float(fine_process7_total_price_td)
        part.fine_process8_total_price=float(fine_process8_total_price_td)
        part.single_process_price=float(one_part_process_price)
        part.total_price=float(total_price)
        db.session.add(part)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '编辑执行成功'})


