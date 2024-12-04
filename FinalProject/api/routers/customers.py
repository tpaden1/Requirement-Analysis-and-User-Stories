from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..models import customers as customer_model
from ..schemas import customers as customer_schema

router = APIRouter(
    tags=["Customers"],
    prefix="/customers"
)

@router.post("/", response_model=customer_schema.Customer)
def create_customer(request: customer_schema.CustomerCreate, db: Session = Depends(get_db)):
    new_customer = customer_model.Customer(
        name=request.name,
        phone_number=request.phone_number,
        address=request.address
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

@router.get("/", response_model=list[customer_schema.Customer])
def read_all_customers(db: Session = Depends(get_db)):
    return db.query(customer_model.Customer).all()

@router.get("/{customer_id}", response_model=customer_schema.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(customer_model.Customer).filter(customer_model.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/{customer_id}", response_model=customer_schema.Customer)
def update_customer(customer_id: int, request: customer_schema.CustomerUpdate, db: Session = Depends(get_db)):
    customer = db.query(customer_model.Customer).filter(customer_model.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    customer.name = request.name or customer.name
    customer.phone_number = request.phone_number or customer.phone_number
    customer.address = request.address or customer.address
    db.commit()
    db.refresh(customer)
    return customer

@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(customer_model.Customer).filter(customer_model.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(customer)
    db.commit()
    return {"detail": "Customer deleted successfully"}
