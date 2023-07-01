from pydantic import BaseModel
from app.models.drink_category import DrinkMethodEnum


class DrinkCategoryModel(BaseModel):
    id: int | None
    name: str | None
    type: DrinkMethodEnum
