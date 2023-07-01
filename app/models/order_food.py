from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class OrderFood(Base):
    __tablename__ = 'order_food'

    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    food_id = Column(Integer, ForeignKey('food.id'), primary_key=True)
