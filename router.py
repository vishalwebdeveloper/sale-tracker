from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import service, schema

router = APIRouter(prefix="/sales", tags=["Sales"])


# CREATE → VALIDATION
@router.post("", response_model=schema.SaleResponse)
def create_sale(sale: schema.SaleCreate, db: Session = Depends(get_db)):
    return service.create_sale(db, sale)

@router.get("/stats", response_model=schema.SalesStatsResponse)
def sales_stats_api(db: Session = Depends(get_db)):
    return service.get_sales_stats(db)

#  GET → NO VALIDATION ERROR NOW
@router.get("", response_model=list[schema.SaleResponse])
def get_sales(phone_model: str = None, color:str = None, db: Session = Depends(get_db)):
    return service.get_sales(db, phone_model,color)


#  GET BY ID → SAFE
@router.get("/{sale_id}", response_model=schema.SaleResponse)
def get_sale(sale_id: int, db: Session = Depends(get_db)):
    result = service.get_sale_by_id(db, sale_id)
    if not result:
        raise HTTPException(status_code=404, detail="Sale not found")
    return result


#  UPDATE → VALIDATION
@router.put("/{sale_id}", response_model=schema.SaleResponse)
def update_sale(sale_id: int, sale: schema.SaleCreate, db: Session = Depends(get_db)):
    updated = service.update_sale(db, sale_id, sale)
    if not updated:
        raise HTTPException(status_code=404, detail="Sale not found")
    return updated


#  DELETE → NO VALIDATION
@router.delete("/{sale_id}")
def delete_sale(sale_id: int, db: Session = Depends(get_db)):
    deleted = service.delete_sale(db, sale_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Sale not found")
    return {"message": "Sale deleted successfully"}



