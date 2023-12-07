from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app: FastAPI = FastAPI()

users = [
    {
        "id": 1,
        "username": "fmesa",
        "name": "Francisco",
        "last_name": "Mesa",
        "email": "fmesa@mail.com",
        "date_of_birth": "2003-01-15",
    },
    {
        "id": 2,
        "username": "dtorres",
        "name": "David",
        "last_name": "Torres",
        "email": "dtorres@mail.com",
        "date_of_birth": "2000-05-21",
    },
    {
        "id": 3,
        "username": "jlopez",
        "name": "Juan",
        "last_name": "Lopez",
        "email": "jlopez@mail.com",
        "date_of_birth": "1999-12-31",
    },
    {
        "id": 4,
        "username": "adiaz",
        "name": "Ana",
        "last_name": "Díaz",
        "email": "adiaz@mail.com",
        "date_of_birth": "1995-06-30",
    },
    {
        "id": 5,
        "username": "jgarcia",
        "name": "Julia",
        "last_name": "Garcia",
        "email": "jgarcia@mail.com",
        "date_of_birth": "2002-11-10",
    }
]


@app.get("/")
async def root() -> object:
    return {"message": "Hola"}


@app.get("/users")
async def get_users() -> object:
    return JSONResponse(content=jsonable_encoder(users))


@app.get("/users/{user_id}")
async def get_user(user_id: int) -> object:
    user = [user for user in users if user["id"] == user_id] or {"message": "User not found"}
    return JSONResponse(content=jsonable_encoder(user))
