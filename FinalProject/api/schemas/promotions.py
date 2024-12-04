from pydantic import BaseModel
from typing import Optional

class PromotionBase(BaseModel):
    promo_code: str
    description: Optional[str]
    discount: float

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    promo_code: Optional[str]
    description: Optional[str]
    discount: Optional[float]

class Promotion(PromotionBase):
    id: int

    class Config:
        orm_mode = True
