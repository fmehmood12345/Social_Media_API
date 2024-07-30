from fastapi import APIRouter
from typing import List
from SM_API.models.post import UserPost, UserPostIn

router = APIRouter()  # fastAPI app

"""Database"""

post_table = {}


# Create post endpoint
@router.post("/post", response_model=UserPost)
async def create_post(post: UserPostIn):
    # data = dict(post)
    data = post.dict()  # defined structure of body
    last_record_id = len(post_table)  # defined post id
    new_post = {**data,
                "id": last_record_id}  # Creates a new dictionary with all the filed and values of the dictionary data and contain their relative ids
    post_table[last_record_id] = new_post
    return new_post


@router.get("/post", response_model=List[UserPost])  # Use List from typing
async def get_all_posts():
    return list(post_table.values())

# # Get decorator - if a client makes a request to the / endpoint, then the return of the root function will be returned
# @app.get("/")
# async def root():  # async def means this function can run more or less at the same time as other functions
#     return {"message": "Hello, world!"}


# An API router is basically the same as a fastAPI app however, instead of running on its own, it can be included into an existing app.
