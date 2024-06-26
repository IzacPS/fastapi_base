# examples
# from typing import List, Optional
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy.orm.properties import ForeignKey
# from app.db.session import Base
#
# class StoreModel(Base):
#     __tablename__ = "store"
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     sname: Mapped[str]
#     image: Mapped[Optional[str]]
#     whatsapp: Mapped[Optional[str]]
#     phone: Mapped[Optional[str]]
#     email: Mapped[Optional[str]]
#     address_id: Mapped[int] = mapped_column(ForeignKey("address.id"))
#
#     address: Mapped["AddressModel"] = relationship(back_populates="store") # type: ignore
#     flyers: Mapped[List["FlyerModel"]] = relationship(back_populates="store") # type: ignore
#
#     def __repr__(self) -> str:
#         return f'<StoreModel({self.id},{self.sname},{self.image},{self.whatsapp},{self.phone},{self.email},{self.address})>'
#
