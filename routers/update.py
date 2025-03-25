from fastapi import APIRouter, HTTPException

from Database.fake_database import users
from models.shema import RegisterUser

update_user_router = APIRouter(prefix="/update", tags=["Редактирование"])


@update_user_router.put("/{user_id}")
async def update_user(*, user_id: str, user: RegisterUser):
    if user_id != users[user_id]:
        raise HTTPException(status_code=404, detail="Not found")
    
    if user.first_name != None:
        users["first_name"] = user.first_name
    
    if user.last_name != None:
        users["last_name"] = user.last_name
    
    if user.email != None:
        users["email"] = user.email
        
    if user.password != None:
        users["password"] = user.password
    
    return {"Data": "success"}