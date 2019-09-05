from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 链接数据库采用pymysq模块
engine=create_engine("mysql+pymysql://root:wangmingdong1225@127.0.0.1:3306/py3_sqlalchemy")
Session = sessionmaker(bind=engine)

session = Session()