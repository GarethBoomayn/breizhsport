from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

# Test the home route
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Breizhsport API"}

# Test retrieving products
def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test creating a new product
def test_create_product():
    product_data = {"name": "Basketball", "description": "Official size basketball", "price": 25.99, "stock": 20}
    response = client.post("/products/", json=product_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Basketball"