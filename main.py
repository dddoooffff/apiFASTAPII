from fastapi import FastAPI

from routers import login, register, update, delete
from Database import fake_database



app = FastAPI()


app.include_router(router=login.login_router)
app.include_router(router=register.register_router)
app.include_router(router=update.update_user_router)
app.include_router(router=delete.delete_user_router)


@app.get("/", tags=["Основная страница"])
async def index():
    return fake_database.users
