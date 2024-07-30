from pydantic import BaseModel  # BaseModel is a class used to define a model. A model is used to validate data

"""Models used to validate incoming and outgoing data"""


class UserPostIn(BaseModel):  # Inheriting from BaseModel
    # This model is used to create a new post and contains the body field.
    body: str


# This model inherits from UserPostIn and adds the id field to uniquely identify each post.
class UserPost(UserPostIn):
    id: int


class CommentIn(BaseModel):
    # This model is used to create a new comment and contains the body field and post_ID field to associate the comment with a post.
    body: str
    post_ID: int


# This model inherits from CommentIn and adds the id field to uniquely identify each comment.
class Comment(CommentIn):
    id: int


# This model combines a post (UserPost) with its comments (list[CommentOut]).
class UserPostWithComments(BaseModel):
    post: UserPost
    comments: list[Comment]

    """
    The data structure of the response is essentially going to look like this:
    {
        "post": {"id": 0, "body": "My Post"}, 
        "comments": [{"id": 2, "post_id": 0, "body": "My Comment"}]
    }
    """
