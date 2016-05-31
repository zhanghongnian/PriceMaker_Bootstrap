# -*- coding:utf-8 -*-

from flask import render_template, jsonify, request
from . import part_type
from .. import db
from ..models import PartType
import json

# 设置客户
@part_type.route('/set_part_types')
def set_part_types():
    return render_template('set_part_types.html')


@part_type.route('/part_type_getdata')
def part_type_getdata():
    part_types = []
    for part_type in PartType.query.all():
        part_types.append(part_type.get_dict())
    return jsonify({'rows': part_types})


@part_type.route('/part_type_add', methods=['POST'])
def part_type_add():
    name = request.form.get('name')
    if PartType.query.filter_by(name=name).first() is not None:
        return jsonify({'result': False, 'message': '此条目已存在'})
    try:
        db.session.add(PartType(name=name))
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '增加操作执行成功'})


@part_type.route('/part_type_delete', methods=['POST'])
def part_type_delete():
    name = request.form.get('name')
    part_type = PartType.query.filter_by(name=name).first()
    if part_type is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    try:
        db.session.delete(part_type)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '增加删除执行成功'})


@part_type.route('/part_type_edit', methods=['POST'])
def part_type_edit():
    old_name = request.form.get('old_name')
    name = request.form.get('name')
    part_type = PartType.query.filter_by(name=old_name).first()
    if part_type is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    try:
        part_type.name = name
        db.session.add(part_type)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '编辑执行成功'})


