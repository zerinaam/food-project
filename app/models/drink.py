from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Drink(Base):
    __tablename__ = "drink"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    photo = Column(String)
    comment = Column(String)

    category_id = Column(Integer, ForeignKey("drink_category.id"))
