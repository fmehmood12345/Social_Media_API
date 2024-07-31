from fastapi import APIRouter, HTTPException
from typing import List
from SM_API.models.post import UserPost, UserPostIn, Comment, CommentIn, UserPostWithComments

router = APIRouter()  # fastAPI app

"""Database"""

post_table = {}
comment_table = {}


def find_post(post_id: int):
    return post_table.get(post_id)


# Create post endpoint
@router.post("/post", response_model=UserPost, status_code=201)
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


@router.post("/comment", response_model=Comment, status_code=201)
async def create_comment(comment: CommentIn):
    post = find_post(comment.post_ID)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    data = comment.dict()  # defined structure of body
    last_record_id = len(comment_table)  # defined post id
    new_comment = {**data,
                   "id": last_record_id}  # Creates a new dictionary with all the filed and values of the dictionary data and contain their relative ids
    comment_table[last_record_id] = new_comment
    return new_comment


@router.get("/post/{post_id}/comment", response_model=List[Comment])
async def get_comments_on_post(post_id: int):
    return [comment for comment in comment_table.values() if comment["post_ID"] == post_id]


@router.get("/post/{post_id}", response_model=UserPostWithComments)
async def get_post_with_comments(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return {
        "post": post,
        "comments": await get_comments_on_post(post_id)
        # await ensures the get_comments_on_post function finishes running, and we get a return before this line complete running
    }

# # Get decorator - if a client makes a request to the / endpoint, then the return of the root function will be returned
# @app.get("/")
# async def root():  # async def means this function can run more or less at the same time as other functions
#     return {"message": "Hello, world!"}


# An API router is basically the same as a fastAPI app however, instead of running on its own, it can be included into an existing app.
