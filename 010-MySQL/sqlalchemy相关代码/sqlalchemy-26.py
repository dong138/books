from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship


# 链接是需要指定要用到的MySQL数据库
engine = create_engine('mysql+pymysql://root:wangmingdong1225@localhost:3306/py3_sqlalchemy_2?charset=utf8')
Base = declarative_base()  # 生成SQLORM基类


# 多对多
class HostToHostUser(Base):
    __tablename__ = 'host_to_host_user'
    nid = Column(Integer, primary_key=True,autoincrement=True)

    host_id = Column(Integer,ForeignKey('host.nid'))
    host_user_id = Column(Integer,ForeignKey('host_user.nid'))
    # 多对多操作
    host = relationship('Host', backref='h')
    host_user = relationship('HostUser', backref='u')


class Host(Base):
    __tablename__ = 'host'
    nid = Column(Integer, primary_key=True,autoincrement=True)
    hostname = Column(String(32))
    port = Column(String(32))
    ip = Column(String(32))


class HostUser(Base):
    __tablename__ = 'host_user'
    nid = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String(32))


def init_db():
    """创建所有的数据表"""
    Base.metadata.create_all(engine)

def drop_db():
    """删除所有的数据表"""
    Base.metadata.drop_all(engine)


# 创建所有的数据库
# init_db()
# 删除所欲的数据表
# drop_db()
# exit()

Session = sessionmaker(bind=engine)
session = Session()

# # 多对多操作

# # 创建Host对象并添加到数据表中
# h1 = Host(hostname='c1', port='22', ip='192.1168.1.1')
# h2 = Host(hostname='c2', port='22', ip='192.1168.1.2')
# h3 = Host(hostname='c3', port='22', ip='192.1168.1.3')
# h4 = Host(hostname='c4', port='22', ip='192.1168.1.4')
# h5 = Host(hostname='c5', port='22', ip='192.1168.1.5')
# session.add_all([h1, h2, h3, h4, h5])
# session.commit()

# # 创建User对象并添加到数据表中
# u1 = HostUser(username='root')
# u2 = HostUser(username='db')
# u3 = HostUser(username='nb')
# u4 = HostUser(username='sb')
# session.add_all([u1, u2, u3, u4])
# session.commit()

# # 将关联数据添加到聚合表中
# session.add_all([
#     HostToHostUser(host=h1, host_user=u1),
#     HostToHostUser(host=h1, host_user=u2),
#     HostToHostUser(host=h1, host_user=u3),
#     HostToHostUser(host=h2, host_user=u2),
#     HostToHostUser(host=h2, host_user=u4),
#     HostToHostUser(host=h2, host_user=u3),
# ])
# session.commit()

# # 1.先在host表中查询c1的nid
# host_obj = session.query(Host).filter(Host.hostname=='c1').first()
# print(host_obj)  # 查询出来的是一个Host对象 <__main__.Host object at 0x108034e10>

# #2 .查询hosttohostuer表中的所有host_id等于c1的nid的对应的host_user_id
# host_2_host_user = session.query(HostToHostUser.host_user_id).filter(HostToHostUser.host_id==host_obj.nid).all()
# print(host_2_host_user)  # [(1,), (2,), (3,)]

# r = zip(*host_2_host_user)
# ids = list(list(r)[0])
# print(ids)  # [1, 2, 3]
# # 通过查到的host_user_id查询hostuser表中的对应的管理员用户名
# users = session.query(HostUser.username).filter(HostUser.nid.in_(ids)).all()
# print(users)

# 1.反向查找,查询host表中c1的信息,会得到一个对象,对象中存在一个已经设置好的虚拟关系:h
host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
print(host_obj)  # <__main__.Host object at 0x107397eb8>

print(host_obj.h)  # [<__main__.HostToHostUser object at 0x107397be0>, <__main__.HostToHostUser object at 0x107397b70>, <__main__.HostToHostUser object at 0x1073b84e0>]

# 2.正向查找,遍历对象属性
for item in host_obj.h:
    print("-" * 20)
    print(item)  # 是HostToHostUser对象
    print(item.host_user)  # <__main__.HostUser object at 0x102b18b38>
    print(item.host_user.username)  # 

session.close()