from sqlalchemy import Column, Integer, String, Enum
from app.db.base_class import Base
from app.utils.enums import DrinkMethodEnum


class DrinkCategory(Base):
    __tablename__ = "drink_category"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(Enum(DrinkMethodEnum))
