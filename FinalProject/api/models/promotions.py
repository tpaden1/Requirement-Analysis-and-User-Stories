from sqlalchemy import Column, Integer, String, Float
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    promo_code = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=True)
    discount = Column(Float, nullable=False)
