# coding=utf-8
# 导入蓝图对象
from . import api
# 导入flask内置的对象
from flask import current_app, jsonify, g, request
from fangkexitong import db
# 导入自定义状态码
from fangkexitong.utils.response_code import RET
# 导入模型类
from fangkexitong.models import Invitation, InvitingPerson, PersonOpen, Visitors, Applicant
# 导入json模块
import json, re
# 导入日期模块
import datetime

@api.route('/users/carry', methods=['GET'])
def get_infomation():
    """访客登记:以往的访客自动填充
    :return:
    """
    try:
        # 获取post请求的json字符串
        info_data = request.get_json()
        # 检查参数的存在
        if not info_data:
            return jsonify(jsonify(success=RET.WRONG, data='没有获取到数据'))
        open_id = info_data.get("open_id")
        invitingperson = InvitingPerson.query.filter_by(open_id=open_id).first()  #  根据open_id查询数据
    except Exception as e:
        current_app.logger.error(e)
        # 写入如果发生异常,需要进行回滚
        db.session.rollback()
        return jsonify(success=RET.WRONG, data='查询数据库失败')
    if invitingperson is None:
        return jsonify(success=RET.WRONG, data='没有用户信息')

    return jsonify(success=RET.OK, data=invitingperson.inviting_info())



@api.route('/users/carry', methods=['POST'])
def post_infomation():
    """
      访客登记,第一个访客是受邀人,需要保存到受邀人表,后面的需要保存到受访人表
      :return:
      """
    # 获取post请求的json字符串
    carry_data = request.get_json()  #  访客可能不是一个人,总是列表
    # 检查参数的存在
    if not carry_data:
        return jsonify(success=RET.WRONG, data='携带访客数据录入失败')
    # 获取详细的参数信息
    data = []
    for i in range(0, len(carry_data)):
        invite_id = carry_data[i].get('invite_id')
        full_name = carry_data[i].get('full_name')
        phone = carry_data[i].get('phone')
        email = carry_data[i].get('email')
        id_type = carry_data[i].get('id_type')
        id_num = carry_data[i].get('id_num')
        company = carry_data[i].get('company')
        if not all([full_name,phone,email,id_num,id_type,company]):
            return jsonify(success=RET.WRONG, data='数据不全')
        if i == 0:  #  查询数据库看是否已经存在  第一个需要添加到受邀人的表
            try:
                invitperon = InvitingPerson.query.filter_by(full_name=full_name,phone=phone).first()
                if invitperon is None:
                    invitingperson = InvitingPerson(full_name=full_name,phone=phone,email=email,id_type=id_type,id_num=id_num,company=company)
            except Exception as e:
                current_app.logger.error(e)
                return jsonify(success=RET.WRONG, data='查询用户信息失败')
            user_id = g.user_id
            user_name = g.user_name
            user_comp = g.user_comp
            personopen = PersonOpen(inperson_id=invitingperson.id,invite_id=invite_id,inperson_name=full_name,user_id=user_id,user_name=user_name,user_comp=user_comp)
            Invitation.query.filter_by(id=invite_id).updata({"state": "已生效"})
            data.append(invitingperson.inviting_info())
        if i != 0:  #  查询数据库看是否已经存在     后面的受访人放到受访人的表
            try:
                visitors = Visitors.query.filter_by(full_name=full_name,phone=phone).first()
                if visitors is None:
                    visitor = Visitors(full_name=full_name,phone=phone,email=email,id_type=id_type,id_num=id_num,company=company,inperson_id=invitingperson.id)
            except Exception as e:
                current_app.logger.error(e)
                return jsonify(success=RET.WRONG, data='查询用户信息失败')
            data.append(visitor.visitor_info())
        try:
            db.session.add(invitingperson)
            db.session.add(personopen)
            db.session.add(visitor)
            db.session.commit()               #   数据库事务
        except Exception as e:
            current_app.logger.error(e)
            # 写入如果发生异常,需要进行回滚
            db.session.rollback()
            return jsonify(success=RET.WRONG, data='保存用户信息失败')

        # data.append({"invite_id": invite_id})
        return jsonify(success=RET.OK, data=data)