# -*- coding:utf-8 -*-

from flask import render_template, jsonify, request
from . import material_shape
from .. import db
from ..models import MaterialShape
import json

# 设置客户
@material_shape.route('/set_material_shapes')
def set_material_shapes():
    return render_template('set_material_shapes.html')


@material_shape.route('/material_shape_getdata')
def material_shape_getdata():
    material_shapes = []
    for material_shape in MaterialShape.query.all():
        material_shapes.append(material_shape.get_dict())
    return jsonify({'rows': material_shapes})


@material_shape.route('/material_shape_add', methods=['POST'])
def material_shape_add():
    name = request.form.get('name')
    if MaterialShape.query.filter_by(name=name).first() is not None:
        return jsonify({'result': False, 'message': '此条目已存在'})
    try:
        db.session.add(MaterialShape(name=name))
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '增加操作执行成功'})


@material_shape.route('/material_shape_delete', methods=['POST'])
def material_shape_delete():
    name = request.form.get('name')
    material_shape = MaterialShape.query.filter_by(name=name).first()
    if material_shape is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    try:
        db.session.delete(material_shape)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '增加删除执行成功'})


@material_shape.route('/material_shape_edit', methods=['POST'])
def material_shape_edit():
    old_name = request.form.get('old_name')
    name = request.form.get('name')
    material_shape = MaterialShape.query.filter_by(name=old_name).first()
    if material_shape is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    try:
        material_shape.name = name
        db.session.add(material_shape)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '编辑执行成功'})


