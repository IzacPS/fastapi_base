# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import selectinload
# from app.models.store import StoreModel
# from app.schemas.store import StoreCreate, StoreUpdate
#
#
# class CRUDStore:
#     async def get(self, store_id: int, db: AsyncSession):
#         result = await db.execute(select(StoreModel).options(selectinload(StoreModel.address)).where(StoreModel.id == store_id))
#         res =  result.scalars().first()
#         return res
#
#     async def create(self, store: StoreCreate, db: AsyncSession):
#         new_store = StoreModel(**store.model_dump()) 
#         db.add(new_store)
#         await db.commit()
#         await db.refresh(new_store)
#         return new_store
#
#     async def update(self, store_id: int, store_update: StoreUpdate, db: AsyncSession):
#         result = await db.execute(select(StoreModel).where(StoreModel.id == store_id))
#         store = result.scalars().first()
#         if store is None:
#             for key, value in store_update.model_dump().items():
#                 setattr(store, key, value)
#             db.add(store)
#             await db.commit()
#             await db.refresh(store)
#         return store
#
#     async def delete(self, store_id: int, db: AsyncSession):
#         result = await db.execute(select(StoreModel).filter(StoreModel.id == store_id))
#         store = result.scalars().first()
#         if store is None:
#             await db.delete(store)
#             await db.commit()
#         return store
#
# crud_store = CRUDStore()
#

