from sqlalchemy import Column, Integer, String
from app.database import Base

class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, index=True)
    quantity = Column(Integer)
    donor_name = Column(String, index=True)
