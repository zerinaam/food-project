from fastapi import APIRouter
from app.db.session import session
from app.models.food_category import FoodCategory
from app.schemas.food_category import FoodCategoryModel

router = APIRouter()


@router.get("/food/category/")
async def get_food_category():
    return session.get(FoodCategory).all()


@router.post("/food/category")
async def add_food_category(food_category_model: FoodCategoryModel):
    food_category = FoodCategory(
        id=food_category_model.id,
        name=food_category_model.name,
        method=food_category_model.method
    )

    session.add(food_category)
    session.commit()
    return "Food category has been added."


@router.get("/food/category/{id}")
async def get_food_category_by_id(id:int):
    return session.query(FoodCategory).filter(FoodCategory.id == id).first()


@router.put("/food/category/{id}")
async def update_food_category_id(id:int, food_category_update: FoodCategoryModel):
    food_category = session.query(FoodCategory).filter(FoodCategory.id == id).first()
    if food_category is None:
        return "Food category with provided id does not exist."

    food_category.name = food_category_update.name if food_category_update.name else food_category.name
    food_category.method = food_category_update.method if food_category_update.method else food_category.method

    session.commit()
    return "Food category has been updated"


@router.delete("/food/category/{id}")
async def delete_food_category(id:int):
    food_category = session.query(FoodCategory).filter(FoodCategory.id == id).first()
    if food_category is None:
        return f"Food category with id {id} does not exist."

    session.delete(food_category)
    session.commit()
    return "Food category has been deleted."




