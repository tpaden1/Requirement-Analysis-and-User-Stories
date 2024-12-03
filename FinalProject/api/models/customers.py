from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    phone_number = Column(String(15), nullable=False)
    address = Column(String(255), nullable=False)


    orders = relationship("Order", back_populates="customer")
