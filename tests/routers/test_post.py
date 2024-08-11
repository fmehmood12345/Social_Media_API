import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from src.main import app


async def create_post(body: str, async_client: AsyncClient) -> dict:
    response = await async_client.post("/create_post", json={
        "body": body})  # sends an asynchronous HTTP POST request to the endpoint /create_post with a JSON payload containing the body text.
    return response.json()


@pytest.fixture()  # Only going to use this when testing a function which requires a post to already exist.
async def created_post(async_client: AsyncClient):
    return await create_post("Test Post",
                             async_client)  # calls the create_post function above with the body "Test Post" and the
    # provided async_client. It waits for the create_post function to complete
    # and returns its result.


@pytest.fixture()
async def created_comment(async_client: AsyncClient,
                          created_post: dict):  # requires a post to already exist so created_post fixture is passed in the parameter
    return await create_post("Test Comment", async_client, created_post["id"])


@pytest.mark.anyio
async def test_create_post():
    test_client_obj = TestClient(app)
    body = "Test Post"
    response = await test_client_obj.post("/create_post", json={"body": body})

    assert response.status_code == 201
    assert {"id": 0, "body": body}.items() <= response.json().items()


@pytest.mark.anyio
async def test_create_post_missing_data(async_client: AsyncClient):
    response = await async_client.post("/create_post", json={})
    assert response.status_code == 422


@pytest.mark.anyio
async def test_get_all_posts(async_client: AsyncClient, created_post: dict):
    response = await async_client.get(
        "/get_all_posts")  # Hitting /get_all_posts endpoint because that is what we are testing

    assert response.status_code == 200
    assert response.json() == [created_post]


# testing if we can create a comment
async def test_create_comment(created_post: dict):
    test_client_obj = TestClient(app)
    body = "Test Comment"
    response = await test_client_obj.post("/create_comment", json={"body": body, "post_id": created_post["id"]})
    assert response.status_code == 201
    assert {
               "id": 0,
               "body": body,
               "post_id": created_post["id"]
           }.items() <= response.json().items()
