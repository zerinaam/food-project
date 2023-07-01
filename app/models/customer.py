from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    street_address = Column(String)
    city = Column(String)
    phone_number = Column(Integer)
    comment = Column(String)

    order = relationship("Order", back_populates="customer")
