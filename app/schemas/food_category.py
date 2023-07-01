from pydantic import BaseModel
from app.models.food_category import FoodMethodEnum


class FoodCategoryModel(BaseModel):
    id: int | None
    name: str | None
    method: FoodMethodEnum
