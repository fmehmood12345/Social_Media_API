import pytest
from httpx import AsyncClient


async def create_post(body: str, async_client: AsyncClient) -> dict:
    response = await async_client.post("/create_post", json={
        "body": body})  # sends an asynchronous HTTP POST request to the endpoint /post with a JSON payload containing the body text.
    return response.json()


@pytest.fixture()  # Only going to use this when testing a function which requires a post to already exist.
async def created_post(async_client: AsyncClient):
    return await create_post("Test Post",
                             async_client)  # calls the create_post function above with the body "Test Post" and the
    # provided async_client. It waits for the create_post function to complete
    # and returns its result.


@pytest.mark.anyio
async def test_create_post(async_client: AsyncClient):
    body = "Test Post"

    response = await async_client.post("/create_post", json={"body": body})

    assert response.status_code == 201
    assert {"id": 0, "body":body}.items() <= response.json().items()

@pytest.mark.anyio
async def test_create_post_missing_data(async_client: AsyncClient):
    response = await async_client.post("/create_post", json={})
    assert response.status_code == 422

@pytest.mark.anyio
async def test_get_all_posts(async_client: AsyncClient, created_post: dict):
    response = await async_client.get("/get_all_posts") # Hitting /get_all_posts endpoint because that is what we are testing

    assert response.status_code == 200
    assert response.json() == [created_post]
