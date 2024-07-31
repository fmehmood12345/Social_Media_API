from typing import AsyncGenerator, Generator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from SM_API.main import app
from SM_API.routers.post import post_table, comment_table

"""The purpose of a fixture is so that the code inside the fixture can be used with any test without having repetition."""


@pytest.fixture(scope="session")# scope="session" means this fixture will only run once in this session.
# For example: Imagine you have a fixture that sets up a database connection, you want this connection to be shared across all your
# tests so that you can avoid the overhead of setting it up and tearing it down for each test
def anyio_backend():
    return "asyncio"


@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)


@pytest.fixture(autouse=True)  # Done autouse=True so that this fixture runs with/for any test
async def db() -> AsyncGenerator:
    post_table.clear()
    comment_table.clear()
    yield

@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url=client.base_url) as ac:
        yield ac
