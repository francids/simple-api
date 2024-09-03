from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json

router = APIRouter()


@router.get("/users")
async def get_users() -> object:
    with open("data/users.json", "r") as file:
        users_data = json.load(file)

    return JSONResponse(content=jsonable_encoder(users_data))


@router.get("/users/{user_id}")
async def get_user(user_id: int) -> object:
    with open("data/users.json", "r") as file:
        users_data = json.load(file)

    user_data = [user for user in users_data if user["id"] == user_id] or None
    if not user_data:
        return JSONResponse(content={"error": "User not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(user_data))
