# -*- coding:utf-8 -*-

from flask import render_template, jsonify, request
from . import measure
from .. import db
from ..models import Measure
import json

# 设置客户
@measure.route('/set_measures')
def set_measures():
    return render_template('set_measures.html')


@measure.route('/measure_getdata')
def measure_getdata():
    measures = []
    for measure in Measure.query.all():
        measures.append(measure.get_dict())
    return jsonify({'rows': measures})


@measure.route('/measure_add', methods=['POST'])
def measure_add():
    name = request.form.get('name')
    if Measure.query.filter_by(name=name).first() is not None:
        return jsonify({'result': False, 'message': '此条目已存在'})
    try:
        db.session.add(Measure(name=name))
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '增加操作执行成功'})


@measure.route('/measure_delete', methods=['POST'])
def measure_delete():
    name = request.form.get('name')
    measure = Measure.query.filter_by(name=name).first()
    if measure is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    try:
        db.session.delete(measure)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '增加删除执行成功'})


@measure.route('/measure_edit', methods=['POST'])
def measure_edit():
    old_name = request.form.get('old_name')
    name = request.form.get('name')
    measure = Measure.query.filter_by(name=old_name).first()
    if measure is None:
        return jsonify({'result': False, 'message': '此条目不存在'})
    try:
        measure.name = name
        db.session.add(measure)
        db.session.commit()
    except Exception as e:
        return jsonify({'result': False, 'message': str(e)})

    return jsonify({'result': True, 'message': '编辑执行成功'})


