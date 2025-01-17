from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text
from pydantic import BaseModel
from app.database import get_db
from app.models.donation import Donation

router = APIRouter()

# Create Pydantic model for request validation
class DonationCreate(BaseModel):
    item_name: str
    quantity: int
    donor_name: str

@router.get("/")
async def get_donations(db: AsyncSession = Depends(get_db)):
    # Use SQLAlchemy's select statement
    query = select(Donation)
    result = await db.execute(query)
    donations = result.scalars().all()
    return {"donations": [{"id": d.id, "item_name": d.item_name,
                         "quantity": d.quantity, "donor_name": d.donor_name}
                         for d in donations]}

@router.post("/")
async def create_donation(donation: DonationCreate, db: AsyncSession = Depends(get_db)):
    new_donation = Donation(
        item_name=donation.item_name,
        quantity=donation.quantity,
        donor_name=donation.donor_name
    )
    db.add(new_donation)
    await db.commit()
    await db.refresh(new_donation)
    return {"message": "Donation added successfully!", "donation": {
        "id": new_donation.id,
        "item_name": new_donation.item_name,
        "quantity": new_donation.quantity,
        "donor_name": new_donation.donor_name
    }}
