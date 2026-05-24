from fastapi import FastAPI
from app.routers import (studio, unit
)

app = FastAPI(
    title="IknFlow API",
    version="1.0.0"
)

app.include_router(studio.router)
app.include_router(unit.router)

@app.get("/")
def root():
    return {"message": "IknFlow API is running"}