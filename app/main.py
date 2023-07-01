from fastapi import FastAPI

from app.routers import customer, drink, drink_category, food, food_category, order

app = FastAPI(
    title="Food",
    version="0.1.0",
)

app.include_router(customer.router)
app.include_router(drink.router)
app.include_router(drink_category.router)
app.include_router(food.router)
app.include_router(food_category.router)
app.include_router(order.router)
