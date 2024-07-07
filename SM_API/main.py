from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  # fastAPI app


# Get decorator - if a client makes a request to the / endpoint, then the return of the root function will be returned
@app.get("/")
async def root():  # async def means this function can run more or less at the same time as other functions
    return {"message": "Hello, world!"}
