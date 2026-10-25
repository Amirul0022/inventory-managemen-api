from fastapi import Header, HTTPException, status
from typing import Optional

async def verify_api_key(x_api_key: Optional[str] = Header(None)) -> dict:
    if x_api_key != "gudang-rahasia-2026":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key tidak valid atau tidak disertakan!"
        )
    return {"user": "admin_inventory", "role": "ADMIN"}