import requests
import os
import pymysql
from faker import Faker
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# note - API key stored as an environment variable.


# SQL Alchemy Stuff
class Product_Family(Base):
    __tablename__ = 'product_family'
    family_id = Column(Integer, primary_key=True)
    name = Column(String(5000))


class Product_Subfamily(Base):
    __tablename__ = 'product_subfamily'
    subfamily_id = Column(Integer, primary_key=True)
    name = Column(String(500))
    family_id = Column(Integer, ForeignKey(Product_Family.family_id))
    family = relationship(Product_Family)


class Products(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product_number = Column(String(100))
    name = Column(String(500))
    description = Column(String(2000))
    uom = Column(String(20))
    manufacturer_id = Column(Integer)
    family_id = Column(Integer, ForeignKey(Product_Subfamily.family_id))
    subfamily_id = Column(Integer, ForeignKey(Product_Subfamily.subfamily_id))
    subfamily = relationship(Product_Subfamily, foreign_keys=[subfamily_id])
    family = relationship(Product_Subfamily, foreign_keys=family_id)

# connect to API and bring back some data
engine = create_engine(
    'mysql+pymysql://michaelkunc:welcome123@localhost/electronics')

Session = sessionmaker(bind=engine)
session = Session()

# url = 'https://octopart.com/api/v3/parts/match?apikey={}&queries=[{{"mpn":"SN7*", "limit":20}}]&pretty_print=true&include[]=short_description&include[]=descriptions'.format(
#     os.environ['API_KEY'])
# r = requests.get(url)
# data = r.json()


# for item in data['results'][0]['items']:
#     product = Products(product_number=item['mpn'],
#                        name=item['brand']['name'],
#                        description=item['short_description'],
#                        uom='Each')
#     session.add(product)
#     session.commit()
#     session.close()

import fake_products

for i in range(0, 10000):
    fake = fake_products.FakeProduct()
    data = Products(product_number=fake.part_number(),
                    name=fake.name(),
                    description=fake.description(),
                    uom=fake.uom())
    session.add(data)
    session.commit()

session.close()
