from typing import Optional, List
from pydantic import BaseModel
from .orders import Order


#Base
class CustomerBase(BaseModel):
    name: str
    phone_number: str
    address: str


class CustomerCreate(CustomerBase):
    pass


# Schema for updating
class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None


# Schema for retrieving
class Customer(CustomerBase):
    id: int
    orders: List[Order] = []

    class Config:
        orm_mode = True
