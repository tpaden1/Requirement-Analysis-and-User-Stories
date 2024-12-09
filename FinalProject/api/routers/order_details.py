from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import order_details as controller
from ..schemas.order_details import OrderDetailCreate, OrderDetailUpdate, OrderDetail
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Order Details'],
    prefix="/orderdetails"
)

@router.post("/", response_model=OrderDetail)
def create_order_detail(request: OrderDetailCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[OrderDetail])
def read_order_details(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{detail_id}", response_model=OrderDetail)
def read_order_detail(detail_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=detail_id)

@router.put("/{detail_id}", response_model=OrderDetail)
def update_order_detail(detail_id: int, request: OrderDetailUpdate, db: Session = Depends(get_db)):
    return controller.update(db, item_id=detail_id, request=request)

@router.delete("/{detail_id}")
def delete_order_detail(detail_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id=detail_id)
