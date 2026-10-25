from fastapi import APIRouter, Depends, HTTPException
from schemas.transaction import TransactionCreate, TransactionResponse
from dependencies.auth import verify_api_key
from routers.items import db_items

router = APIRouter(prefix="/api/v1/transactions", tags=["Transactions"])
db_transactions = []

@router.post("/", response_model=TransactionResponse, status_code=201)
async def create_transaction(payload: TransactionCreate, current_user: dict = Depends(verify_api_key)):
    item_index = next((index for (index, d) in enumerate(db_items) if d["id"] == payload.item_id), None)
    
    if item_index is None:
        raise HTTPException(status_code=404, detail="Barang tidak ditemukan")

    item = db_items[item_index]

    if payload.type == "OUT":
        if item["current_stock"] < payload.quantity:
            raise HTTPException(status_code=400, detail="Stok tidak mencukupi untuk transaksi OUT")
        db_items[item_index]["current_stock"] -= payload.quantity
    else:
        db_items[item_index]["current_stock"] += payload.quantity

    new_tx = {
        "id": len(db_transactions) + 1,
        "status": "SUCCESS",
        **payload.model_dump()
    }
    db_transactions.append(new_tx)
    return new_tx
