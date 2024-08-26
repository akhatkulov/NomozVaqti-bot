from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, BigInteger, func, VARCHAR
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
import conf

# Database setup
engine = create_engine(conf.DB_URI)
Base = declarative_base()

# Session factory
Session = sessionmaker(bind=engine)

# Models
class User(Base):
    __tablename__ = 'user_ptime_u2s'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cid = Column(BigInteger, unique=True)
    manzil = Column(String, default="0")
    step = Column(String, default="!!!")

class Groups(Base):
    __tablename__ = 'group_ptime_u2s'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cid = Column(VARCHAR(50), unique=True)

class Channels(Base):
    __tablename__ = 'channels_ptime_u2s'
    id = Column(Integer, primary_key=True, autoincrement=True)
    link = Column(String, default="None", unique=True)

# Create tables
Base.metadata.create_all(engine)

# Function to get all user CIDs
def get_all_user():
    with Session() as session:
        x = session.query(User.cid).all()
        res = [i[0] for i in x]
        return res

# Function to get the count of users
def user_count():
    with Session() as session:
        x = session.query(func.count(User.id)).first()
        return x[0]

# Function to create a new user
def create_user(cid):
    with Session() as session:
        try:
            user = User(cid=int(cid), manzil="0", step="!!!")
            session.add(user)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error: {e}")

# Function to create a new group
def create_group(cid):
    with Session() as session:
        try:
            group = Groups(cid=str(cid))
            session.add(group)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error: {e}")

# Function to get the location of a user
def get_location(cid):
    with Session() as session:
        x = session.query(User.manzil).filter_by(cid=cid).first()
        return x[0] if x else None

# Function to update the location of a user
def put_location(cid, x_location):
    with Session() as session:
        try:
            user = session.query(User).filter_by(cid=cid).first()
            if user:
                user.manzil = x_location
                session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error: {e}")

# Function to get the step of a user
def get_step(cid):
    with Session() as session:
        x = session.query(User).filter_by(cid=cid).first()
        return x.step if x else None

# Function to update the step of a user
def put_step(cid, step):
    with Session() as session:
        try:
            user = session.query(User).filter_by(cid=cid).first()
            if user:
                user.step = str(step)
                session.commit()
                return True
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error: {e}")
            return False

# Function to add a new channel
def put_channel(channel: str):
    with Session() as session:
        try:
            x = Channels(link=channel)
            session.add(x)
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error: {e}")
            return False

# Function to get all channels
def get_channel():
    with Session() as session:
        x = session.query(Channels).all()
        res = [i.link for i in x]
        return res

# Function to get all channels with IDs
def get_channel_with_id():
    with Session() as session:
        try:
            channels = session.query(Channels).all()
            res = "\n".join([f"ID: {channel.id} \nLink: @{channel.link}" for channel in channels])
            return res
        except SQLAlchemyError as e:
            print(f"Error: {e}")
            return ""

# Function to delete a channel by ID
def delete_channel(ch_id):
    with Session() as session:
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
