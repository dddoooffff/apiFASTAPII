from fastapi import APIRouter, HTTPException

from Database.fake_database import users

delete_user_router = APIRouter(prefix="/delete", tags=["Удаление"])


@delete_user_router.delete("/{user_id}")
async def delete_user(user_id: str):
    del users[user_id]
    
    return {"Data": "Пользователь удален"}