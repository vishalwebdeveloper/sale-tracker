from pydantic import BaseModel, Field, field_validator
import re
from decimal import Decimal
from datetime import date, datetime

# create api request validation schemas
class SaleBase(BaseModel):
    customer_name: str = Field(..., min_length=2, max_length=150)
    phone_model: str
    color: str
    storage_gb: int
    price: Decimal
    store_location: str
    
    @field_validator("customer_name")
    def validate_name(cls, v):
        if not re.match(r"^[A-Za-z ]+$", v):
            raise ValueError("Customer name must contain only letters")
        return v.strip()

    @field_validator("phone_model")
    def validate_model(cls, v):
        allowed = [
            "iPhone 13", "iPhone 14", "iPhone 15", "iPhone 16", "iPhone 17",
            "iPhone 15 Pro", "iPhone 15 Pro Max",
            "iPhone 16 Pro", "iPhone 16 Pro Max",
            "iPhone 17 Pro", "iPhone 17 Pro Max"
        ]

        v_clean = v.strip().lower()

        for model in allowed:
            if v_clean == model.lower():
                return model  # normalize

        raise ValueError(f"Phone model must be one of {allowed}")

    @field_validator("storage_gb")
    def validate_storage(cls, v):
        if v not in [64, 128, 256, 512, 1024]:
            raise ValueError("Invalid storage")
        return v

    @field_validator("price")
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError("Price must be > 0")
        return v

    @field_validator("store_location")
    def validate_location(cls, v):
        return v.strip()


# This is the class we use for both create and update, since they have the same fields
class SaleCreate(SaleBase):
    pass

class SaleUpdate(SaleBase):
    pass


# Get api responses without validation showing database value
class SaleResponse(BaseModel):
    id: int
    customer_name: str
    phone_model: str
    color: str
    storage_gb: int
    price: Decimal
    store_location: str
    sale_date:date
    created_at:datetime
    class Config:
        from_attributes = True

class SalesStatsResponse(BaseModel):
    total_sales: int
    total_revenue: Decimal
    average_price: Decimal
    most_popular_model: str | None