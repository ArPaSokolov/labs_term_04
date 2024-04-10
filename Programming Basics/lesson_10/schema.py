import datetime as dt

from sqlalchemy import create_engine

from sqlalchemy import Column, ForeignKey, CheckConstraint
from sqlalchemy import Integer, String, Boolean, DateTime, Numeric, SmallInteger

from sqlalchemy.orm import declarative_base, relationship, sessionmaker


Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False, unique=True, index=True)
    email = Column(String(200), nullable=False, unique=True, index=True)
    created_on = Column(DateTime(), default=dt.datetime.now)
    updated_on = Column(DateTime(), default=dt.datetime.now, onupdate=dt.datetime.now)
    
    orders = relationship("Order", back_populates="customer")

    def __str__(self):
        return f"<{self.id}> {self.first_name} {self.last_name}: {self.username}/{self.email}"

    def __repr__(self):
        return f"<{self.id}> {self.first_name} {self.last_name}"


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2),  nullable=False)
    quantity = Column(Integer())
    # или так, но без строки ниже:
    # quantity = Column(Integer(), CheckConstraint("quantity > 0"))
    __table_args__ = (CheckConstraint("quantity > 0"),)

    def __str__(self):
        return f"<{self.id}> {self.name}: {self.cost_price}/{self.selling_price} {self.quantity}"

    def __repr__(self):
        return f"<{self.id}> {self.name}"


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey("customers.id"))
    date_placed = Column(DateTime(), default=dt.datetime.now)

    customer = relationship("Customer")
    details = relationship("OrderLine", back_populates="order")
  

class OrderLine(Base):
    __tablename__ = 'order_lines'
    order_id = Column(Integer(), ForeignKey('orders.id'), primary_key=True)
    item_id = Column(Integer(), ForeignKey('items.id'), primary_key=True)
    quantity = Column(SmallInteger())

    order = relationship("Order")
    item = relationship("Item")


engine = create_engine("sqlite:///My Database/shop.db?echo=True")

if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

factory = sessionmaker(bind=engine)
session = factory()