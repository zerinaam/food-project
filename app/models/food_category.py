from sqlalchemy import Column, Integer, String, Enum
from app.db.base_class import Base
from app.utils.enums import FoodMethodEnum


class FoodCategory(Base):
    __tablename__ = "food_category"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    method = Column(Enum(FoodMethodEnum))
