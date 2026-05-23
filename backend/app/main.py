from fastapi import FastAPI

app = FastAPI(
    title="IknFlow API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "IknFlow API is running"}