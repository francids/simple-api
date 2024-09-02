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


@router.get("/posts/{post_id}")
async def get_post(post_id: int) -> object:
    with open("data/posts.json", "r") as file:
        posts_data = json.load(file)

    post_data = [post for post in posts_data if post["id"] == post_id] or None
    if not post_data:
        return JSONResponse(content={"error": "Post not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(post_data))
