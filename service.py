from sqlalchemy.orm import Session
from sqlalchemy import func
from model import IphoneSale
from schema import SaleCreate
from datetime import date
from decimal import Decimal,ROUND_HALF_UP
# CREATE
def create_sale(db: Session, sale: SaleCreate):
    data = sale.model_dump()
    data["sale_date"] = date.today()
    db_sale = IphoneSale(**data)
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale


# GET ALL data with the query parameter for filtering by phone_model
def get_sales(db: Session, phone_model: str = None, color:str = None):
    query = db.query(IphoneSale)

    if phone_model:
        query = query.filter(IphoneSale.phone_model.ilike(f"%{phone_model}%"))
    if color:
        query = query.filter(IphoneSale.color.ilike(f"%{color}%"))

    return query.all()


def get_sale_by_id(db: Session, sale_id: int):
    return db.query(IphoneSale).filter(IphoneSale.id == sale_id).first()


# UPDATE
def update_sale(db: Session, sale_id: int, data: SaleCreate):
    sale = get_sale_by_id(db, sale_id)
    if not sale:
        return None

    for key, value in data.model_dump().items():
        setattr(sale, key, value)

    db.commit()
    db.refresh(sale)
    return sale


# DELETE
def delete_sale(db: Session, sale_id: int):
    sale = get_sale_by_id(db, sale_id)
    if not sale:
        return None

    db.delete(sale)
    db.commit()
    return True

def get_sales_stats(db: Session):
    total_sales = db.query(func.count(IphoneSale.id)).scalar() or 0
    
    total_revenue = db.query(func.sum(IphoneSale.price)).scalar() or Decimal("0")

    avg_price = db.query(func.avg(IphoneSale.price)).scalar() or Decimal("0")

    total_revenue = total_revenue.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
    avg_price = avg_price.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
    popular_model = (
        db.query(
            IphoneSale.phone_model,
            func.count(IphoneSale.phone_model).label("count")
        )
        .group_by(IphoneSale.phone_model)
        .order_by(func.count(IphoneSale.phone_model).desc())
        .first()
    )

    most_popular_model = popular_model[0] if popular_model else None

    return {
        "total_sales": total_sales,
        "total_revenue": total_revenue,
        "average_price": avg_price,
        "most_popular_model": most_popular_model
    }