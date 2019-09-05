from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker


# 链接是需要指定要用到的MySQL数据库
engine = create_engine('mysql+pymysql://root:wangmingdong1225@localhost:3306/py3_sqlalchemy?charset=utf8')
Base = declarative_base()  # 生成SQLORM基类


class User(Base):

    # 对应MySQL中数据表的名字
    __tablename__ = 'users'

    # 创建字段
    id = Column(Integer, primary_key=True)  #users表中的id字段(主键)
    username = Column(String(64), nullable=False, index=True)  # uers表中的username字段
    password = Column(String(64), nullable=False)  # users表中的password字段
    email = Column(String(64), nullable=False, index=True)  # users表中的email字段(有索引)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)

# 创建userinfo表（所有表结构）
# Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)  # 创建与数据库的会话，返回的是一个类
# 创建session对象
session = DBSession()  # 生成链接数据库的实例

# # 获取所有数据
# obj = session.query(User).all()

# # print(type(obj))  # 查询出来的类型是 <class 'list'>

# # 说明：
# # obj查询出来的是一个列表，其中数据为 User类的实例对象
# for temp in obj:
# 	print("-" * 20)
# 	# print(temp)  # 此时temp为User类的实例对象
# 	# print(type(temp))  # 类型是 <class '__main__.User'>
# 	print(temp.id)
# 	print(temp.username)
# 	print(temp.password)
# 	print(temp.email)
 
# # 获取指定数据
# obj = session.query(User).filter(User.id==1).one()
# print(obj.id)
# print(obj.username)
# print(obj.password)
# print(obj.email)

# print("-" * 20)

# obj = session.query(User).filter(User.id==4).one()
# print(obj.id)
# print(obj.username)
# print(obj.password)
# print(obj.email)
 
# 获取返回数据的第一行
obj = session.query(User).first()
print(obj.id)
print(obj.username)
print(obj.password)
print(obj.email)
 
# # 查询ID>1的所有名字
# session.query(User.name).filter(User.id>1).all()
 
# # 通过索引取出数据
# q1 = session.query(User.name).all()[1:2]
 
# # 根据id降序排列
# q1 = session.query(User).order_by(-User.id).all()
 
# # 查询user表中id是1,3的姓名
# q1 = session.query(User.name).filter(User.id.in_([1,3])).all()
 
# # 模糊查询,%匹配多个字符,_匹配单个字符
# q1 = session.query(User.name).filter(User.name.like('%h__')).all()
 
# # 计算个数,返回查询的数量
# q1 = session.query(User).count()
 
# # 逻辑与查询
# from sqlalchemy import and_
# obj = session.query(User).filter(and_(User.id==1,User.name =='a')).all()
# # 提交结果
# session.commit()
# session.close()
 
# # 逻辑或查询
# from sqlalchemy import or_
# obj = session.query(User).filter(or_(User.id==1,User.name =='c')).all()
# # 提交结果
# session.commit()
# session.close()
 
# # 排序查询(按照id倒序显示name)
# obj = session.query(User.name).order_by(-User.id).all()
# # # 提交结果
# session.commit()
# session.close()


session.close()