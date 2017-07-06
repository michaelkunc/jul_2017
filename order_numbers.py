import random
from string import ascii_uppercase, digits


def order_number():
    """Return fake order number in the following format 714-EO1-56237-B"""
    prefix = ''.join(random.sample(digits, 3))
    mid = ''.join(random.sample(ascii_uppercase, 2) + random.sample(digits, 1))
    end = ''.join(random.sample(digits, 5))
    post = ''.join(random.sample(ascii_uppercase, 1))
    return '{0}-{1}-{2}-{3}'.format(prefix, mid, end, post)


# code for returning a random id for insertion into the customer fields in
# the order headers table

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

engine = create_engine(
    'mysql+pymysql://michaelkunc:welcome123@localhost/demo')

Session = sessionmaker(bind=engine)
session = Session()


def get_random_id(table):
    """Takes a SQLAlchemy class name as a parameter."""
    return session.query(table).order_by(func.rand()).first().id
