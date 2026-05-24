from fastapi import FastAPI
from app.routes import (studio_router, unit_router)


app = FastAPI(
    title="IknFlow API",
    version="1.0.0"
)

app.include_router(studio_router)
app.include_router(unit_router)

@app.get("/")
def root():
    return {"message": "IknFlow API is running"}