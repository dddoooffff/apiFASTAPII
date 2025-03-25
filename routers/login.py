from fastapi import APIRouter, HTTPException

from models.shema import LoginUser
from Database.fake_database import users

login_router = APIRouter(prefix="/login", tags=["Вход в систему"])

@login_router.post("/")
async def login_user(user_login: LoginUser):
    for user in users.values():
        if user_login.email == user["email"] and user_login.password == user["password"]:
            return {"Data", "success"}
            
    
    raise HTTPException(status_code=401, detail="invalid credentials")