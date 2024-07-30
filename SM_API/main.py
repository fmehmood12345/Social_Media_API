from fastapi import FastAPI
from SM_API.routers.post import router as post_router

app = FastAPI()  # fastAPI app

app.include_router(post_router)


