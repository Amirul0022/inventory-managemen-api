from pydantic import BaseModel, Field, field_validator
from typing import Optional

class ItemBase(BaseModel):
    name: str = Field(..., min_length=3)
    category: str
    sku: str = Field(..., description="Format: INV-FST-XXXX")

    @field_validator("sku")
    @classmethod
    def validate_sku(cls, value: str) -> str:
        if not value.startswith("INV-FST-"):
            raise ValueError("SKU tidak valid, harus diawali INV-FST-")
        return value

class ItemCreate(ItemBase):
    initial_stock: int = Field(default=0, ge=0)

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None

class ItemResponse(ItemBase):
    id: int
    current_stock: int