from fastapi import APIRouter
from app.db.session import session
from app.models.food import Food
from app.schemas.food import FoodModel

router = APIRouter()


@router.get("/food")
async def get_food():
    return session.query(Food).all()


@router.post("/food")
async def add_food(food_model: FoodModel):
    food = Food(
        id=food_model.id,
        name=food_model.name,
        photo=food_model.photo,
        preparation_time=food_model.preparation_time,
        comment=food_model.comment,
        category_id=food_model.category_id
    )

    session.add(food)
    session.commit()
    return "Food has been added"


@router.get("/food/{id}")
async def get_food_by_id(id: int):
    return session.query(Food).filter(Food.id == id).first()


@router.put("/food/{id}")
async def update_food_id(id: int, food_update: FoodModel):
    food = session.query(Food).filter(Food.id == id).first()
    if food is None:
        return "Food with provided id does not exist."

    food.name = food_update.name if food_update.name else food.name
    food.photo = food_update.photo if food_update.photo else food.photo
    food.preparation_time = food_update.preparation_time if food_update.preparation_time else food.preparation_time
    food.comment = food_update.comment if food_update.comment else food.comment
    food.category_id = food_update.category_id if food_update.category_id else food.category_id

    session.commit()
    return "Food has been updated."


@router.delete("/food/{id}")
async def delete_food_by_id(id: int):
    food = session.query(Food).filter(Food.id == id).first()
    if food is None:
        return f"Food with id {id} does not exist."
    session.delete(food)
    session.commit()
    return "Food has been deleted."














