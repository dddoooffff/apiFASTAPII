from pydantic import BaseModel, EmailStr
from typing import Optional
from fastapi import Path

class RegisterUser(BaseModel):
    first_name: str = Path(max_length=15)
    last_name: str | None = Path(max_length=20)
    email: EmailStr
    password: str = Path(max_length=20)
    again_password: str

class LoginUser(BaseModel):
    email: EmailStr
    password: str = Path(max_length=20)
    
class UpdateUser(BaseModel):
    first_name: str | None = Path(max_length=15)
    last_name: str | None = Path(max_length=20)
    password: str | None = Path(max_length=20)