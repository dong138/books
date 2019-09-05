from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()  # 生成SQLORM基类


# 多对多
class HostToHostUser(Base):
    __tablename__ = 'host_to_host_user'
    nid = Column(Integer, primary_key=True,autoincrement=True)

    host_id = Column(Integer,ForeignKey('host.nid'))
    host_user_id = Column(Integer,ForeignKey('host_user.nid'))
    # # 多对多操作
    # host = relationship('Host', backref='h')
    # host_user = relationship('HostUser', backref='u')


class Host(Base):
    __tablename__ = 'host'
    nid = Column(Integer, primary_key=True,autoincrement=True)
    hostname = Column(String(32))
    port = Column(String(32))
    ip = Column(String(32))
    ####最简单的方式,添加此行就行:
    host_user = relationship('HostUser',secondary=HostToHostUser.__table__, backref='host')


class HostUser(Base):
    __tablename__ = 'host_user'
    nid = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String(32))