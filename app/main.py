from fastapi import FastAPI
from app.routes.donation_routes import router as donation_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to GenerousHands API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}


app.include_router(donation_router, prefix="/donations", tags=["Donations"])
