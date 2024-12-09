from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas.orders import OrderCreate, OrderUpdate, Order
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)

@router.post("/", response_model=Order)
def create_order(request: OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[Order])
def read_orders(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{order_id}", response_model=Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=order_id)

@router.put("/{order_id}", response_model=Order)
def update_order(order_id: int, request: OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db, item_id=order_id, request=request)

@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id=order_id)
