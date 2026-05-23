from fastapi import FastAPI
from app.routers import studio

app = FastAPI(
    title="IknFlow API",
    version="1.0.0"
)

app.include_router(studio.router)

@app.get("/")
def root():
    return {"message": "IknFlow API is running"}