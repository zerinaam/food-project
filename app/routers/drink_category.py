from fastapi import APIRouter
from app.db.session import session
from app.models.drink_category import DrinkCategory
from app.schemas.drink_category import DrinkCategoryModel

router = APIRouter()


@router.get("/drink/category")
async def get_drink_category():
    return session.query(DrinkCategory).all()


@router.post("/drink/category")
async def add_drink_category(drink_category_model: DrinkCategoryModel):
    drink_category = DrinkCategory(
        id=drink_category_model.id,
        name=drink_category_model.name,
        type=drink_category_model.type
    )

    session.add(drink_category)
    session.commit()
    return "Drink category has been added."


@router.get("/drink/category/{id}")
async def get_drink_by_id(id: int):
    return session.query(DrinkCategory).filter(DrinkCategory.id == id).first()


@router.put("/drink/category/{id}")
async def update_drink_category_id(id: int, drink_category_update: DrinkCategoryModel):
    drink_category = session.query(DrinkCategory).filter(DrinkCategory.id == id).first()
    if drink_category is None:
        return "Drink category with provided id does not exist."

    drink_category.name = drink_category_update.name if drink_category_update.name else drink_category.name
    drink_category.method = drink_category_update.type if drink_category_update.type else drink_category.type

    session.commit()
    return "Drink category has been updated"


@router.delete("/drink/category/{id}")
async def delete_drink_category(id: int):
    drink_category = session.query(DrinkCategory).filter(DrinkCategory.id == id).first()
    if drink_category is None:
        return f"Drink category with id {id} does not exist."
    session.delete(drink_category)
    session.commit()
    return "Drink category has been deleted."

