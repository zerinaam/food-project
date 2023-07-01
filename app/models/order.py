from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from app.models.order_food import OrderFood
from app.models.order_drink import OrderDrink


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    food = relationship("Food", secondary="order_food")
    drinks = relationship("Drink", secondary="order_drink")
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="order")
