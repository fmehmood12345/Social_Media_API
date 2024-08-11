from fastapi import FastAPI
from src.routers.socialmedia_posts import router as post_router
from src.routers.comments import router as comments_router
app = FastAPI()  # fastAPI app

app.include_router(post_router, prefix="/posts")
app.include_router(comments_router, prefix="/comments")


