from sqlalchemy import Column, Integer, String

from src.infrastructure.models.base import Base


class UserDao(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(99), index=True)
    email = Column(String(99), index=True)

    # items = relationship("Item", back_populates="owner")
