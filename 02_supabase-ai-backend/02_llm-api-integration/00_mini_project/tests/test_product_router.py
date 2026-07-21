from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_product_create_returns_created_product():
    product = {"id": 1, "name": "키보드", "price": 50000}

    response = client.post("/product/create", json=product)

    assert response.status_code == 200
    assert response.json() == product


def test_product_get_returns_product():
    response = client.get("/product/get/7")

    assert response.status_code == 200
    assert response.json() == {
        "id": 7,
        "name": "크록스",
        "price": 30000,
    }


def test_product_get_all_returns_products():
    response = client.get("/product/getall")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 100,
            "name": "pants01",
            "price": 20000,
        }
    ]


def test_product_create_rejects_invalid_body():
    response = client.post(
        "/product/create",
        json={"id": 1, "name": "키보드"},
    )

    assert response.status_code == 422

