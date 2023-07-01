from pydantic import BaseModel


class FoodModel(BaseModel):
    id: int | None
    name: str | None
    photo: str | None
    preparation_time: int | None
    comment: str | None
    category_id: int
