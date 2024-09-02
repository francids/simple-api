from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routes.users import router as users_router
from routes.posts import router as posts_router


app: FastAPI = FastAPI()


@app.get("/")
async def root() -> object:
    return JSONResponse(content={"OK": True})


@app.get("/ping")
async def ping() -> object:
    return JSONResponse(content={"ping": "pong"})


app.include_router(users_router)
app.include_router(posts_router)
