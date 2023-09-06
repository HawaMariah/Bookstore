#book store
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///bookstore.db', echo=False)

Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()

class Books(Base):
    __tablename__ =  'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(), nullable=False)
    author = Column(String(), nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer,nullable=False)

    orders = relationship('orders', back_populates='book')

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    email_address = Column(String(), nullable=False)
    phone_number = Column(Integer, nullable=False)

    orders = relationship('orders', back_populates='user')

class orders(Base):
    __tablename__ = 'orders'
   
    order_id = Column(Integer,primary_key=True )
    user_id = Column(Integer, ForeignKey('users.id'))
    books_id = Column(Integer, ForeignKey('books.id'))
    quantity = Column(Integer,nullable=False)
    order_date = Column(Integer, nullable=False)
    total_amount = Column(Integer, nullable=False)
    
    user = relationship('Users', back_populates='orders')
    book = relationship('Books', back_populates='orders')
 
class exchange(Base):
    __tablename__ = 'exchange'
    new_id = Column(Integer, primary_key=True)
    original_id = Column(Integer, nullable= False)
    order_date = Column(Integer, nullable=False)

#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)