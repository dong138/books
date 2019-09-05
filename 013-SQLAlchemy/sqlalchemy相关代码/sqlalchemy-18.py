from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship


# 链接是需要指定要用到的MySQL数据库
engine = create_engine('mysql+pymysql://root:wangmingdong1225@localhost:3306/py3_sqlalchemy?charset=utf8')
Base = declarative_base()  # 生成SQLORM基类


class Parent(Base):
    __tablename__ = 'parent_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    # 可以通过parent_table表查child_table,数据库中不会创建children字段,只是建立里联系
    # 参数backref相当于给类Child添加了一个属性，在查询的时候可以通过Child.parents属性获取child_table表关联的所有parent_table表
    children = relationship('Child', backref = 'parents')


class Child(Base):
    __tablename__ = 'child_table'
    id = Column(Integer, primary_key=True,autoincrement=True)
    age = Column(Integer)
    parent_id = Column(Integer, ForeignKey('parent_table.id'))

# 创建userinfo表（所有表结构）
Base.metadata.create_all(engine)
# DBSession = sessionmaker(bind=engine)  # 创建与数据库的会话，返回的是一个类
# # 创建session对象
# session = DBSession()  # 生成链接数据库的实例

# # 查询出符合条件的一个对象
# obj = session.query(Parent).filter(Parent.id==1).one()
# print(obj.children)
# # 通过对象属性children，查出这个对象的所有关联age字段值
# for i in obj.children:
#     print(i.age)
 
# # 查询出符合条件的一个对象
# obj = session.query(Child).filter(Child.id==2).one()
# # 打印对象中的关联
# print(obj.parents.name)
 
# # 内关联查询出Parent.id == Child.parent_id的结果
# q6 = session.query(Parent).join(Child).filter(Parent.id == Child.parent_id).all()

# session.close()