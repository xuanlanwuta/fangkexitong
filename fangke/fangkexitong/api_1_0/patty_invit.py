# coding=utf-8
# 导入蓝图对象
from . import api
# 导入flask内置的对象
from flask import current_app, jsonify, g, request
from fangkexitong import db
# 导入自定义状态码
from fangkexitong.utils.response_code import RET
# 导入模型类
from fangkexitong.models import Invitation, Users
# 导入json模块
import json, re
# 导入日期模块
import datetime
# 数据库连接
@api.route('/u', methods=['GET'])
def holle():
    try:
        user = Users(username="xuanlanwuta",password="77585214aq",full_name="姜道强",phone="13793801038",company="上海臻言")
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print(e)
    return '{"a":"hello"}'