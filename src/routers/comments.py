from fastapi import APIRouter, HTTPException
from typing import List
from src.models.post import Comment, CommentIn, UserPostWithComments
from src.routers.socialmedia_posts import find_post, create_post, get_all_posts, post_table


router = APIRouter()  # fastAPI app

"""Database"""

comment_table = {}

@router.post("/create_comment", response_model=Comment, status_code=201)
async def create_comment(comment: CommentIn):
    post = find_post(comment.post_ID)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    data = dict(comment) # defined structure of body
    last_record_id = len(comment_table)  # defined post id
    new_comment = {**data,
                   "id": last_record_id}  # Creates a new dictionary with all the filed and values of the dictionary data and contain their relative ids
    comment_table[last_record_id] = new_comment
    return new_comment


@router.get("/post/{post_id}/get_all_comments", response_model=List[Comment])
async def get_comments_on_post(post_id: int):
    return [comment for comment in comment_table.values() if comment["post_ID"] == post_id]


@router.get("/get_posts_with_comments/{post_id}", response_model=UserPostWithComments)
async def get_post_with_comments(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return {
        "post": post,
        "comments": await get_comments_on_post(post_id)
        # await ensures the get_comments_on_post function finishes running, and we get a return before this line complete running
    }


# An API router is basically the same as a fastAPI app however, instead of running on its own, it can be included into an existing app.

