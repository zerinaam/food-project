from pydantic import BaseModel
from pydantic.schema import datetime

from app.schemas.drink import DrinkModel
from app.schemas.food import FoodModel


class OrderModel(BaseModel):
    id: int | None
    created_at: datetime | None
    food: list[FoodModel]
    drinks: list[DrinkModel]
    customer_id: int | None
