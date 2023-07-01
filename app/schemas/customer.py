from pydantic import BaseModel


class CustomerModel(BaseModel):
    id: int | None
    first_name: str | None
    last_name: str | None
    street_address: str | None
    city: str | None
    phone_number: int | None
    comment: str | None
