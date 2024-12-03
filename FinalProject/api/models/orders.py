from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    description = Column(String(300), nullable=True)


    order_details = relationship("OrderDetail", back_populates="order")
    customer = relationship("Customer", back_populates="orders")
