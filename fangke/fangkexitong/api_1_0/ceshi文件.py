# coding=utf-8
# 导入日期模块
import pymssql

# 数据库连接
con = pymssql.connect(host='176.16.1.6', user='visitor', password='12345678', database='visitor')
#
# # 打开游标
# cur = conn.cursor()
#
# if not cur:
#     raise Exception('数据库连接失败！')
#
# sSQL = 'SELECT * FROM TB'
#
# # 执行sql，获取所有数据
# cur.execute(sSQL)
# result = cur.fetchall()
#
# # 1.result是list，而其中的每个元素是 tuple
# print(type(result), type(result[0]))
#
# # 2.
# print('\n\n总行数：' + str(cur.rowcount))
#
# # 3.通过enumerate返回行号
# for i, (id, name, v) in enumerate(result):
#     print('第 ' + str(i + 1) + ' 行记录->>> ' + str(id) + ':' + name + ':' + str(v))
#
# # 4.修改数据
# cur.execute("insert into tb(id,name,score) values(9,'历史',75)")
# cur.execute("update tb set score=95 where id=7")
# conn.commit()  # 修改数据后提交事务
#
# # 再查一次
# cur.execute(sSQL)
#
# # 5.一次取一条数据,cur.rowcount为-1
# r = cur.fetchone()
# i = 1
#
# print('\n')
#
# while r:
#     id, name, v = r  # r是一个元祖
#     print('第 ' + str(i) + ' 行记录->>> ' + str(id) + ':' + name + ':' + str(v))
#     r = cur.fetchone()
#     i += 1
#
# conn.close()
cur=con.cursor()
cur.execute("select 1")
print cur.fetchall()
cur.close()
con.close()