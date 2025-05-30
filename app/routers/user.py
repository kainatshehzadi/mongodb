from typing import List
from fastapi import APIRouter, HTTPException
from app.models import User
from app.db.database import user_collection
from passlib.context import CryptContext

router = APIRouter()  

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=User)
async def register_user(user: User):
    existing_user = await user_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = pwd_context.hash(user.password)
    user_dict = user.dict()
    user_dict["password"] = hashed_password

    await user_collection.insert_one(user_dict)
    return user 

@router.get("/users", response_model=List[User])
async def get_users():
    users = []
    cursor = user_collection.find()
    async for document in cursor:
        document.pop("_id", None)  
        users.append(document)     
    return users
