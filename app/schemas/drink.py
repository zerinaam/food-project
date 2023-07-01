from pydantic import BaseModel


class DrinkModel(BaseModel):
    id: int
    name: str
    photo: str
    comment: str
    category_id: int
