from fastapi import FastAPI
from app.routers import user

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "hi vercel deploy fastapi app successfully."}

app.include_router(user.router)
