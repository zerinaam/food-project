from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class OrderDrink(Base):
    __tablename__ = 'order_drink'

    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    drink_id = Column(Integer, ForeignKey('drink.id'), primary_key=True)
