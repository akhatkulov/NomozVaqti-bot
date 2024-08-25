from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, BigInteger, func,VARCHAR
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
import conf
engine = create_engine(conf.DB_URI)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user_ptime'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cid = Column(BigInteger, unique=True)
    manzil = Column(String, default="0")
    step = Column(String,default="!!!")

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

session = Session()

def get_all_user():
    try:
        x = session.query(User.cid).all()
        res = [i[0] for i in x]
        return res
    finally:
        session.close()

def user_count():
    try:
        x = session.query(func.count(User.id)).first()
        return x[0]
    finally:
        session.close()

def create_user(cid):
    try:
        user = User(cid=int(cid), manzil="0",step="!!!")
        session.add(user)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

def create_group(cid):
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
    x = session.query(User.manzil).first()
    return x[0]

def put_location(cid, x_location):
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
    
def get_step(cid):
    try:
        x = session.query(User).filter_by(cid=cid).first()
        return x.step if x else None
    finally:
        session.close()

def put_step(cid, step):
    try:
        x = session.query(User).filter_by(cid=cid).first()
        if x:
            x.step = str(step)
            session.commit()
            return True
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
        return False




def put_channel(channel: str):
    try:
        x = Channels(link=channel)
        session.add(x)
        session.commit()
        return True
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
        return False

def get_channel():
    try:
        x = session.query(Channels).all()
        res = [i.link for i in x]
        return res
    finally:
        session.close()

def get_channel_with_id():
    try:
        x = session.query(Channels).all()
        res = ""
        for channel in x:
            res += f"\nID: {channel.id} \nLink: @{channel.link}"
        return res
    finally:
        session.close()

def delete_channel(ch_id):
    try:
        x = session.query(Channels).filter_by(id=int(ch_id)).first()
        if x:
            session.delete(x)
            session.commit()
            return True
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
        return False