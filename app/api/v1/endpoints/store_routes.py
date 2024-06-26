# examples
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.db.session import get_db
# from app.schemas.store import StoreCreate, StoreSchema, StoreUpdate
# from app.crud.crud_store import crud_store
#
# store_router = APIRouter()
#
#
# @store_router.get("/{store_id}", response_model=StoreSchema)
# async def get_store_by_id(store_id: int, db: AsyncSession = Depends(get_db)):
#     store = await crud_store.get(store_id, db)
#     if store is None:
#         raise HTTPException(status_code=404, detail="Store not found")
#     return store

