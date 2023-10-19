from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from src.infrastructure.models.base import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(99), index=True)
    description = Column(String(1024), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # owner = relationship("User", back_populates="items")
