import os

os.environ["DATABASE_URL"] = "sqlite:///./test_board.db"

from fastapi.testclient import TestClient

from app.database import Base, engine
from app.main import app


def setup_function():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def teardown_module():
    Base.metadata.drop_all(bind=engine)
    engine.dispose()
    if os.path.exists("test_board.db"):
        os.remove("test_board.db")


def test_post_crud():
    with TestClient(app) as client:
        created = client.post(
            "/posts", json={"title": "첫 글", "content": "내용", "author": "홍길동"}
        )
        assert created.status_code == 201
        post_id = created.json()["id"]

        listed = client.get("/posts?page=1&size=10")
        assert listed.status_code == 200
        assert listed.json()["total"] == 1
        assert listed.json()["items"][0]["id"] == post_id

        detail = client.get(f"/posts/{post_id}")
        assert detail.status_code == 200
        assert detail.json()["title"] == "첫 글"

        updated = client.patch(f"/posts/{post_id}", json={"title": "수정된 글"})
        assert updated.status_code == 200
        assert updated.json()["title"] == "수정된 글"

        deleted = client.delete(f"/posts/{post_id}")
        assert deleted.status_code == 204
        assert client.get(f"/posts/{post_id}").status_code == 404


def test_validation_and_not_found():
    with TestClient(app) as client:
        assert client.post("/posts", json={"title": "", "content": "", "author": ""}).status_code == 422
        assert client.get("/posts/999").status_code == 404

