from fastapi import APIRouter, HTTPException
from typing import Optional
from Database.fake_database import users
from models.shema import UpdateUser

update_user_router = APIRouter(prefix="/update", tags=["Редактирование"])


@update_user_router.put("/{user_id}")
async def update_user(*, user_id: int, user: Optional[UpdateUser] = None):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Not found")
    
    if user is None:
        return {"Data": "No data provided for update"}
    
    if user.first_name is not None:
        users[user_id]["first_name"] = user.first_name
    
    if user.last_name is not None:
        users[user_id]["last_name"] = user.last_name
        
    if user.password is not None:
        users[user_id]["password"] = user.password
    
    return {"Data": "success"}