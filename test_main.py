# Import FastAPI's test client — lets us fake HTTP requests like GET, POST, etc.
from fastapi.testclient import TestClient

# Import your FastAPI app instance from main.py (must be defined as app = FastAPI())
from main import app

# Create a fake client that lets us interact with your app in test mode
client = TestClient(app)

# --------------------
# Test #1: Check if the root ("/") endpoint works and returns correct metadata
# --------------------
def test_root():
    # Simulate a GET request to "/"
    response = client.get("/")

    # Check if status code is 200 (OK). If not, this test fails.
    assert response.status_code == 200

    # Convert the response to JSON and check if the word "FastAPI" is in the "service" field
    assert "FastAPI" in response.json()["service"]

# --------------------
# Test #2: Check if numeric order route returns correct drink
# --------------------
def test_get_order_by_number():
    # Simulate GET to /order/15 → should return Brown Sugar drink
    response = client.get("/order/15")

    # Check for HTTP 200 success
    assert response.status_code == 200

    # Check if "Brown Sugar" appears in the drink field of the JSON response
    assert "Brown Sugar" in response.json()["drink"]

# --------------------
# Test #3: Check if custom string-based order returns correct drink
# --------------------
def test_get_custom_order():
    # Simulate GET to /custom_order/matcha
    response = client.get("/custom_order/matcha")

    # Make sure it succeeded (status 200)
    assert response.status_code == 200

    # Check that the returned result includes the expected drink name
    assert "Strawberry Matcha" in response.json()["result"]

# --------------------
# Test #4: POST an order and make sure data was handled correctly
# --------------------
def test_post_submit_order():
    # Define a fake order we want to send to the API
    payload = {
        "name": "Hani",
        "drink": "Crunchy Choco Boba",
        "topping": "Tapioca"
    }

    # Send a POST request to /submit_order with the JSON payload
    response = client.post("/submit_order", json=payload)

    # Confirm the request was successful (200 OK)
    assert response.status_code == 200

    # Now assert that the API echoed back exactly what we sent:
    assert response.json()["your_drink"] == payload["drink"]
    assert "Order received for Hani" in response.json()["message"]
