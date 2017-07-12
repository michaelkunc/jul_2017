import pymysql
from faker import Faker
from sqlalchemy import Column, String, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
import fake_data
from sqlalchemy.sql.expression import func
import time


# Table Def
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


class ProductCosts(Base):
    __tablename__ = 'product_costs'
    cost_id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    mtl_cost = Column(Numeric)
    labor_cost = Column(Numeric)
    burden_cost = Column(Numeric)

# Hydrate the tables
engine = create_engine(
    'mysql+pymysql://michaelkunc:welcome123@localhost/electronics')

Session = sessionmaker(bind=engine)
session = Session()


def populate_families():
    for k, v in fake_data.Product.FAMILIES.items():
        data = Product_Family(family_id=k,
                              name=v)
        session.add(data)
        session.commit()
    session.close()
    print('product_family table has been populated.')


def populate_subfamilies():
    for i in fake_data.Product.SUBFAMILIES:
        data = Product_Subfamily(name=i, family_id=random.choice(
            list(fake_data.Product.FAMILIES.keys())))
        session.add(data)
        session.commit()
    session.close()
    print('product_subfamily table has been populated.')


def populate_products(number):
    print('Populating products table.')
    for i in range(0, number):
        fake = fake_data.Product()
        row = session.query(Product_Subfamily).order_by(func.rand()).first()
        subfamily = (row.subfamily_id, row.family_id)
        data = Products(product_number=fake.part_number(),
                        name=fake.name(),
                        description=fake.description(),
                        uom=fake.uom(),
                        subfamily_id=subfamily[0],
                        family_id=subfamily[1])
        session.add(data)
        session.commit()
    session.close()
    print('products table has been populated.')


def populate_prices():
    for i in session.query(Products.product_id):
        data = ProductCosts(product_id=i[0],
                            mtl_cost=round(random.uniform(.1, 10), 2),
                            labor_cost=round(
                                random.uniform(.1, 10), 2),
                            burden_cost=round(
                                random.uniform(.1, 10), 2)
                            )
        session.add(data)
        session.commit()
    session.close()
    print('product_costs table has been populated.')


# populate_families()
# populate_subfamilies()
# populate_products(2000)
# # calling prices 3 times to generate some historical data
# populate_prices()
# time.sleep(5)
# populate_prices()
# time.sleep(5)
# populate_prices()
