from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Food(Base):
    __tablename__ = "food"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    photo = Column(String)
    preparation_time = Column(Integer)
    comment = Column(String)

    category_id = Column(Integer, ForeignKey("food_category.id"))
