from fastapi import FastAPI
from pydantic import BaseModel  # BaseModel is a class used to define a model. A model is used to validate data
from typing import List
app = FastAPI()  # fastAPI app




"""Database"""
post_table = {}


# Create post endpoint
@app.post("/post", response_model=UserPost)
async def create_post(post: UserPostIn):
    # data = dict(post)
    data = post.dict()  # defined structure of body
    last_record_id = len(post_table)  # defined post id
    new_post = {**data,
                "id": last_record_id}  # Creates a new dictionary with all the filed and values of the dictionary data and contain their relative ids
    post_table[last_record_id] = new_post
    return new_post


@app.get("/post", response_model=List[UserPost])  # Use List from typing
async def get_all_posts():
    return list(post_table.values())

# # Get decorator - if a client makes a request to the / endpoint, then the return of the root function will be returned
# @app.get("/")
# async def root():  # async def means this function can run more or less at the same time as other functions
#     return {"message": "Hello, world!"}
