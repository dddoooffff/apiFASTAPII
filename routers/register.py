from fastapi import APIRouter, HTTPException

from Database.fake_database import users, current_id
from models.shema import RegisterUser

register_router = APIRouter(prefix="/register", tags=["Регистрация"])



@register_router.post("/")
async def register(user: RegisterUser):
    global current_id
    
    if user.password != user.again_password:
        raise HTTPException(status_code=400, detail="Повторный пароль не верен")
    
    user_data = user.model_dump()
    user_data.pop("again_password")
    user_data["id"] = current_id
    users[current_id] = user_data
    
    current_id += 1
    
    return {"Data": "Success"}
    
    
    