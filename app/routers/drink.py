from fastapi import APIRouter
from app.db.session import session
from app.models.drink import Drink
from app.schemas.drink import DrinkModel

router = APIRouter()


@router.get("/drink")
async def get_drink():
    return session.query(Drink).all()


@router.post("/drink")
async def add_drink(drink_model: DrinkModel):
    drink = Drink(
        id=drink_model.id,
        name=drink_model.name,
        photo=drink_model.photo,
        comment=drink_model.comment,
        category_id=drink_model.category_id
    )

    session.add(drink)
    session.commit()
    return "Drink has been added."


@router.get("/drink/{id}")
async def get_drink_by_id(id: int):
    return session.query(Drink).filter(Drink.id == id).first()


@router.put("/drink/{id}")
async def update_drink_id(id:int, drink_update: DrinkModel):
    drink = session.query(Drink).filter(Drink.id == id).first()
    if drink is None:
        return "Drink with provided id does not exist."

    drink.name = drink_update.name if drink_update.name else drink.name
    drink.photo = drink_update.photo if drink_update.photo else drink.photo
    drink.comment = drink_update.comment if drink_update.comment else drink.comment
    drink.category_id = drink_update.category_id if drink_update.category_id else drink.category_id

    session.commit()
    return "Drink has been updated."


@router.delete("/drink/{id}")
async def delete_drink(id:int):
    drink = session.query(Drink).filter(Drink.id == id).first()
    if drink is None:
        return f"Drink with id {id} does not exist."
    session.delete(drink)
    session.commit()
    return "Drink has been deleted."


