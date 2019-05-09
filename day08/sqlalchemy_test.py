# 安装sqlalchemy包
#  activate zpython-0426  激活项目
#  conda install sqlalchemy


from sqlalchemy import Column, INTEGER, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    """ Object - Relationship Mapping"""

    __tablename__ = 'user' # 表和类之间的映射


    id = Column(INTEGER, autoincrement=True, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)


    # toString()
    def __str__(self):
        print(self.id, self.email, self.password)
        return ''


# 数据库类型+数据库驱动名：//账号：口令@服务器：端口号/数据库名
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/db_python')

DBSession = sessionmaker(bind=engine)

spike = User(email='spike@tom.com', password='123')

session = DBSession()

session.add(spike)  # sql


# select * from db_python.user where id = 1
user = session.query(User).filter(User.id == 1).one()

print(user.id)
print(user.email)
print(user.password)

print(user)


session.commit() # 提交事务
session.close()
