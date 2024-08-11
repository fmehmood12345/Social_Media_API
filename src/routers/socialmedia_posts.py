from fastapi import APIRouter
from typing import List
from src.models.post import UserPost, UserPostIn

router = APIRouter()  # fastAPI app

"""Database"""

post_table = {}

def find_post(post_id: int):
    return post_table.get(post_id)


# Create post endpoint
@router.post("/create_post", response_model=UserPost, status_code=201)
async def create_post(post: UserPostIn):
    data = dict(post)  # defined structure of body
    last_record_id = len(post_table)  # defined post id
    new_post = {**data,
                "id": last_record_id}  # Creates a new dictionary with all the filed and values of the dictionary data and contain their relative ids
    post_table[last_record_id] = new_post
    return new_post


@router.get("/get_all_posts", response_model=List[UserPost])  # Use List from typing
async def get_all_posts():
    return list(post_table.values())
