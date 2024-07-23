"""Models used to validate incoming and outgoing data"""


class UserPostIn(BaseModel):  # Inheriting form BaseModel

    # Defining fields in this model
    body: str


# Inheriting body field in the UserPost Class. UserPost class is used to give each post a unique identifier
class UserPost(UserPostIn):
    id: int