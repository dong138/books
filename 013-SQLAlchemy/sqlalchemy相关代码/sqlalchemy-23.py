from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship


# 链接是需要指定要用到的MySQL数据库
engine = create_engine('mysql+pymysql://root:wangmingdong1225@localhost:3306/py3_sqlalchemy_2?charset=utf8')
Base = declarative_base()  # 生成SQLORM基类


#一对多
class Group(Base):
    __tablename__ = 'group'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String(32))

class User(Base):
    __tablename__ = 'user'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    group_id = Column(Integer,ForeignKey('group.nid'))
    ###虚拟创建关系,relationship  一般是跟foreginkey 在一起使用
    group = relationship("Group", backref='users')

    #自定义输出方式
    def __repr__(self):
        temp = '%s-%s:%s'%(self.nid,self.name,self.group_id)
        return temp

# 创建userinfo表（所有表结构）
# Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)  # 创建与数据库的会话，返回的是一个类
# 创建session对象
session = DBSession()  # 生成链接数据库的实例

# 插入数据
g1 = Group(caption='研发')
g2 =  Group(caption='测试')
session.add_all([g1, g2])

session.add_all([
    User(name='老王', group=g1),
    User(name='老闫', group=g1),
    User(name='老马', group=g2),
    User(name='老叶', group=g2)
])

session.commit()

session.close()