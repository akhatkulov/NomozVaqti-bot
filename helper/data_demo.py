from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, BigInteger, func,VARCHAR
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("postgresql://postgres:1945@localhost/postgres")
Base = declarative_base()


class User(Base):
    __tablename__ = 'user_ptime'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cid = Column(BigInteger, unique=True)
    manzil = Column(String, default="0")

class Groups(Base):
    __tablename__ = 'group_ptime'
    id = Column(Integer,primary_key=True,autoincrement=True)
    cid = Column(VARCHAR(50),unique=True)


class Channels(Base):
    __tablename__ = 'channels_ptime'
    id = Column(Integer, primary_key=True, autoincrement=True)
    link = Column(String, default="None", unique=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def get_all_user():
    session = Session()
    try:
        x = session.query(User.cid).all()
        res = [i[0] for i in x]
        return res
    finally:
        session.close()

def user_count():
    session = Session()
    try:
        x = session.query(func.count(User.id)).first()
        return x[0]
    finally:
        session.close()

def create_user(cid):
    session = Session()
    try:
        user = User(cid=int(cid), manzil="0")
        session.add(user)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

def create_group(cid):
    session = Session()
    try:
        user = Groups(cid=int(cid))
        session.add(user)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()
def get_location(cid):
    session = Session()
    x = session.query(User.manzil).first()
    return x
def put_location(cid, x_location):
    session = Session()
    try:
        x = session.query(User).filter_by(cid=cid).first()
        if x:
            x.manzil = x_location
            session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()
    
def get_channel():
    session = Session()
    try:
        x = session.query(Channels).all()
        res = [i.link for i in x]
        return res
    finally:
        session.close()