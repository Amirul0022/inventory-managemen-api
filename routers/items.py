from fastapi import APIRouter, Depends, HTTPException
from schemas.item import ItemCreate, ItemResponse, ItemUpdate
from dependencies.auth import verify_api_key

router = APIRouter(prefix="/api/v1/items", tags=["Items"])
db_items = []  # In-memory dummy database

@router.post("/", response_model=ItemResponse, status_code=201)
async def create_item(payload: ItemCreate, current_user: dict = Depends(verify_api_key)):
    new_item = {"id": len(db_items) + 1, "current_stock": payload.initial_stock, **payload.model_dump()}
    db_items.append(new_item)
    return new_item

@router.get("/", response_model=list[ItemResponse])
async def get_items():
    """Mengambil semua daftar barang (Bisa diakses publik tanpa API Key)"""
    return db_items

@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    """Mengambil detail satu barang berdasarkan ID"""
    for item in db_items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Barang tidak ditemukan")

@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int, current_user: dict = Depends(verify_api_key)):
    """Menghapus barang (Hanya untuk Admin)"""
    for i, item in enumerate(db_items):
        if item["id"] == item_id:
            del db_items[i]
            return None
    raise HTTPException(status_code=404, detail="Barang tidak ditemukan")