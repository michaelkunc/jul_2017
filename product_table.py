import pymysql
from faker import Faker
from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Boolean, Date
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


class PriceList(Base):
    __tablename__ = 'price_lists'
    price_list_id = Column(Integer, primary_key=True)
    active = Column(Boolean)
    list_start_date = Column(Date)
    list_end_date = Column(Date)


class ProductsPrices(Base):
    __tablename__ = 'products_prices'
    price_id = Column(Integer, primary_key=True)
    price_list_id = Column(Integer, ForeignKey(PriceList.price_list_id))
    product_id = Column(Integer, ForeignKey(Products.product_id))
    list_price = Column(Numeric)


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


def populate_price_lists():
    data = [PriceList(active=0, list_start_date='2015-01-01', list_end_date='2015-12-31'),
            PriceList(active=0, list_start_date='2016-01-01',
                      list_end_date='2016-12-31'),
            PriceList(active=1, list_start_date='2017-01-01', list_end_date='2017-12-31')]
    for d in data:
        time.sleep(1)
        session.add(d)
        session.commit()
    session.close()
    print('price_lists has been populated.')


def populate_product_prices():
    for i in session.query(Products.product_id):
        for x in session.query(PriceList.price_list_id):
            data = ProductsPrices(price_list_id=x[0],
                                  product_id=i[0],
                                  list_price=round(random.uniform(1, 100), 2)
                                  )

            session.add(data)
            session.commit()

    session.close()
    print('products_prices has been populated.')

populate_families()
populate_subfamilies()
populate_products(2000)
# calling prices 3 times to generate some historical data
populate_prices()
time.sleep(1)
populate_prices()
time.sleep(1)
populate_prices()

populate_price_lists()
populate_product_prices()
