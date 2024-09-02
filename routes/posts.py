from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json

router = APIRouter()


@router.get("/posts")
async def get_posts() -> object:
    with open("data/posts.json", "r") as file:
        posts_data = json.load(file)

    return JSONResponse(content=jsonable_encoder(posts_data))
