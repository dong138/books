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
#   print("-" * 20)
#   # print(temp)  # 此时temp为User类的实例对象
#   # print(type(temp))  # 类型是 <class '__main__.User'>
#   print(temp.id)
#   print(temp.username)
#   print(temp.password)
#   print(temp.email)
 
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
 
# # 获取返回数据的第一行
# obj = session.query(User).first()
# print(obj.id)
# print(obj.username)
# print(obj.password)
# print(obj.email)
 
# # 查询ID>1的所有名字
# obj = session.query(User.username).filter(User.id>1).all()
# # print(type(obj))  # 类型是 <class '__main__.User'>
# for temp in obj:
#     # print(temp.id)  # 不能查询，因为在上面的查询中指定了是username字段，而没有指定其他的
#     print(temp.username)
#     # print(temp.password)  # 不能查询，因为在上面的查询中指定了是username字段，而没有指定其他的
#     # print(temp.email)  # 不能查询，因为在上面的查询中指定了是username字段，而没有指定其他的
 
# # 通过索引取出数据
# q1 = session.query(User.username).all()[1:4]
# print(q1)
 
# # 根据id升序排列
# obj = session.query(User).order_by(User.id).all()
# for temp in obj:
#   print("*" * 5)
#   print(temp.id)
#   print(temp.username)
#   print(temp.password)
#   print(temp.email)

# print("-" * 20)

# # 根据id降序排列
# obj= session.query(User).order_by(-User.id).all()
# for temp in obj:
#   print("*" * 5)
#   print(temp.id)
#   print(temp.username)
#   print(temp.password)
#   print(temp.email)

 
# # 查询user表中id是1,3的姓名
# obj = session.query(User.username).filter(User.id.in_([1,3])).all()
# for temp in obj:
#   print(temp.username)


# # 创建新User对象
# new_user1 = User(username='sha', password="123456", email="shasha@163.com")
# new_user2 = User(username='shaxuan', password="123456", email="shaxuan@163.com")
# new_user3 = User(username='lili', password="112233", email="lili@163.com")
# new_user4 = User(username='feifei', password="132143245", email="feifei@163.com")
# new_user5 = User(username='shan', password="535211", email="shan@163.com")
# new_user6 = User(username='shapigou', password="535211", email="shapigou@163.com")
# # 添加到session
# session.add_all([new_user1, new_user2, new_user3, new_user4, new_user5, new_user6])
# # 提交即保存到数据库
# session.commit()
 
# 模糊查询,%匹配多个字符,_匹配单个字符
obj = session.query(User.username).filter(User.username.like('%h%')).all()
for temp in obj:
    print(temp.username)

print("-" * 20)

obj = session.query(User.username).filter(User.username.like('%h___')).all()
for temp in obj:
    print(temp.username)
 
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