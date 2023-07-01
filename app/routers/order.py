from fastapi import APIRouter
from app.db.session import session
from app.models.order import Order
from app.schemas.order import OrderModel

router = APIRouter()


@router.get("/order")
async def get_orders():
    return session.query(Order).all()


@router.post("/order")
async def add_order(order_model: OrderModel):
    order = Order(
        id=order_model.id,
        created_at=order_model.created_at,
        customer_id=order_model.customer_id,
    )

    session.add(order)
    session.commit()
    return "Order has been added."


@router.get("/order/{id}")
async def get_order_by_id(id: int):
    return session.query(Order).filter(Order.id == id).first()


@router.put("/order/{id}")
async def update_order_id(id: int, order_update: OrderModel):
    order = session.query(Order).filter(Order.id == id).first()
    if order is None:
        return "Order with provided id does not exist."

    order.created_at = order_update.created_at if order_update.created_at else order.created_at
    order.customer_id = order_update.customer_id if order_update.customer_id else order.customer_id

    session.commit()
    return "Order has been updated."


@router.delete("/order/{id}")
async def delete_order(id: int):
    order = session.query(Order).filter(Order.id == id).first()
    if order is None:
        return f"Oder with id {id} does not exist."
    session.delete(order)
    session.commit()
    return "Order has been deleted."
