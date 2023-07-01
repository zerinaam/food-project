from fastapi import APIRouter
from app.db.session import session
from app.models.customer import Customer
from app.schemas.customer import CustomerModel

router = APIRouter()


@router.get("/customer")
async def get_customers():
    return session.query(Customer).all()


@router.post("/customer")
async def add_customer(customer_model: CustomerModel):
    customer = Customer(
        id=customer_model.id,
        first_name=customer_model.first_name,
        last_name=customer_model.last_name,
        street_address=customer_model.street_address,
        city=customer_model.city,
        phone_number=customer_model.phone_number,
        comment=customer_model.comment
    )

    session.add(customer)
    session.commit()
    return "Customer has been added."


@router.get("/customer/{id}")
async def get_customer_by_id(id: int):
    return session.query(Customer).filter(Customer.id == id).first()


@router.put("/customer/{id}")
async def update_customer_id(id: int, customer_update: CustomerModel):
    customer = session.query(Customer).filter(Customer.id == id).first()
    if customer is None:
        return "Customer with provided id does not exist."

    customer.first_name = customer_update.first_name if customer_update.first_name else customer.first_name
    customer.last_name = customer_update.last_name if customer_update.last_name else customer.last_name
    customer.street_address = customer_update.street_address if customer_update.street_address else customer.street_address
    customer.city = customer_update.city if customer_update.city else customer.city
    customer.phone_number = customer_update.phone_number if customer_update.phone_number else customer.phone_number
    customer.comment = customer_update.comment if customer_update.comment else customer.comment

    session.commit()
    return "Customers has been updated."


@router.delete("/customer/{id}")
async def delete_customer(id: int):
    customer = session.query(Customer).filter(Customer.id == id).first()
    if customer is None:
        return f"Customer with id {id} does not exist."

    session.delete(customer)
    session.commit()
    return "Customer has been deleted."

