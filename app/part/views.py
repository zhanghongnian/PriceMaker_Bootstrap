# -*- coding:utf-8 -*-

from flask import render_template, jsonify, request
from . import part
from .. import db
from ..models import Material, Client, MaterialPrice, Machine, \
MachinePrice, Part, Measure, PartType, MaterialShape
import json


@part.route('/part_simple')
def part_simple():
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
        print(material.name)
    machines = []
    for machine in Machine.query.all():
        machines.append(machine.name)
        print(machine.name)

    return render_template('part_simple.html', 
        measures=measures, part_types=part_types,
        material_shapes=material_shapes, materials=materials,
        machines=machines, clients=clients)


@part.route('/part_get_material_price', methods=['POST'])
def part_get_material_price():
    client = Client.query.filter_by(name=request.form.get('client')).first()
    material = Material.query.filter_by(name=request.form.get('material')).first()
    if client is not None and material is not None:
        client_id = client.id
        material_id = material.id
        materialprice = MaterialPrice.query.filter_by(client_id=client_id).filter_by(material_id=material_id).first()
        if materialprice is not None:
            price = materialprice.price
            return jsonify({'result': True, 'price':price})
    return jsonify({'result': False, 'price':""})


@part.route('/part_get_material_density', methods=['POST'])
def part_get_material_density():
    material = Material.query.filter_by(name=request.form.get('material')).first()
    if material is not None:
        return jsonify({'result': True, 'density':material.density})
    return jsonify({'result': False, 'density':""})


@part.route('/part_get_machine_price', methods=['POST'])
def part_get_machine_price():
    client = Client.query.filter_by(name=request.form.get('client')).first()
    machine = Machine.query.filter_by(name=request.form.get('machine')).first()
    if client is not None and machine is not None:
        machineprice = MachinePrice.query.filter_by(client_id=client.id).filter_by(machine_id=machine.id).first()
        return jsonify({'result': True, 'price':machineprice.price})
    return jsonify({'result': False, 'price':""})

