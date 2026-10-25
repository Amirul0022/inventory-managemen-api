from pydantic import BaseModel, Field, field_validator

class TransactionCreate(BaseModel):
    item_id: int
    quantity: int = Field(..., gt=0, description="Jumlah barang harus lebih dari 0")
    type: str = Field(..., description="Isi dengan 'IN' atau 'OUT'")

    @field_validator("type")
    @classmethod
    def validate_type(cls, value: str) -> str:
        if value not in ["IN", "OUT"]:
            raise ValueError("Tipe transaksi hanya boleh 'IN' atau 'OUT'")
        return value

class TransactionResponse(TransactionCreate):
    id: int
    status: str
