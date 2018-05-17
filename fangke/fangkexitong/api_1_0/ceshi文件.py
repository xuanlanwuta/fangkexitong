# coding=utf-8
# 导入日期模块
from fangkexitong.models import Users
from fangkexitong import db
# 数据库连接


user = Users(username="xuanlanwuta",password="77585214aq",full_name="姜道强",phone="13793801038",company="上海臻言")

db.session.add(user)
db.session.commit()