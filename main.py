from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "service": "FastAPI Boba Order API",
        "status": "running",
        "version": "1.0.0",
        "description": "This API lets you order boba drinks by number or name, and submit your own custom boba order.",
        "routes": {
            "GET /order/{ordernum}": "Get a drink recommendation by order number (1–100)",
            "GET /custom_order/{drink_name}": "Request a drink by keyword (brown, matcha, peach)",
            "POST /submit_order": "Submit a custom drink order (name, drink, topping)",
            "GET /docs": "Interactive API docs"
        },
        "maintainer": "✨ Hani Ahmed"
    }



# For Order Numbered Drinks (1-100)

@app.get("/order/{ordernum}")
def get_order_by_number(ordernum: int):
    if ordernum < 1:
        return {"error": "❌ Invalid order number. Must be 1 or higher."}

    if 1 <= ordernum <= 20:
        drink = "🧋 Brown Sugar Milk Tea"
    elif 21 <= ordernum <= 50:
        drink = "🍓 Strawberry Matcha Latte"
    else:
        drink = "🍑 Peach Oolong Tea"

    return {
        "order_number": ordernum,
        "drink": drink,
        "served_by": "✨ Hanii! ✨",
        "how_we_decide": "1–20 = Brown Sugar, 21–50 = Strawberry Matcha, 51+ = Peach Oolong"
    }

@app.get("/custom_order/{drink_name}")
def get_order_by_name(drink_name: str):
    if drink_name == "brown":
        drink = "🧋 Brown Sugar Milk Tea"
    elif drink_name == "matcha":
        drink = "🍓 Strawberry Matcha Latte"
    elif drink_name == "peach":
        drink = "🍑 Peach Oolong Tea"
    else:
        drink = "😵 Sorry, that drink isn't on the menu!"
        return {
            "your_choice": drink_name,
            "result": drink,
            "menu_hint": "Try brown, matcha, or peach 🍹",
            "served_by": "✨ Hanii! ✨"
        }

    return {
        "your_choice": drink_name,
        "result": drink,
        "menu_hint": "Try brown, matcha, or peach 🍹",
        "served_by": "✨ Hanii! ✨"
    }

# Step 4.5 – POST Endpoint for Order Submission
class BobaOrder(BaseModel):
    name: str
    drink: str
    topping: str

@app.post("/submit_order")
def submit_order(order: BobaOrder):
    return {
        "message": f"🧋 Order received for {order.name}!",
        "your_drink": order.drink,
        "topping": order.topping,
        "served_by": "✨ Hanii! ✨"
    }