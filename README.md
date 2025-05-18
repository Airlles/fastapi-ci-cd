![CI](https://github.com/Airlles/bobacloud-api/actions/workflows/python-app.yml/badge.svg)

# FastAPI Boba Order Microservice

```
                                             .--.
                                          .-(    ).   ☁️
                                         (___.__)__)  
      
                     ____        _            ____ _                 _ 
                    | __ )  ___ | |__   __ _ / ___| | ___  _   _  __| |
                    |  _ \ / _ \| '_ \ / _` | |   | |/ _ \| | | |/ _` |
                    | |_) | (_) | |_) | (_| | |___| | (_) | |_| | (_| |
                    |____/ \___/|_.__/ \__,_|\____|_|\___/ \__,_|\__,_|

```

A lightweight, testable REST API built with **FastAPI** for placing and retrieving fictional boba drink orders. Built as a showcase project to demonstrate backend fundamentals, automated testing, and CI/CD integration.

## 🌐 Live Demo

🟢 **View the live API:**  
[https://fastapi-boba-api.onrender.com](https://fastapi-boba-api.onrender.com)

## ⚙️ Tech Stack

- **Framework:** FastAPI (Python 3.12)  
- **Web Server:** Uvicorn  
- **Testing:** Pytest + HTTPX  
- **CI/CD:** GitHub Actions  
- **Deployment:** Render (Free Tier)  
- **Docs:** Swagger/OpenAPI (`/docs`)

## 📦 API Features

| Route                        | Method | Description                                        |
|-----------------------------|--------|----------------------------------------------------|
| `/`                         | GET    | API metadata and status                           |
| `/order/{ordernum}`         | GET    | Get a drink by order number (1–100)               |
| `/custom_order/{drink_name}`| GET    | Get a drink by name keyword (e.g., `matcha`)      |
| `/submit_order`             | POST   | Submit a full custom order (JSON body)            |
| `/docs`                     | GET    | Swagger UI for interacting with all routes        |

## 🔧 Example Usage

### `GET /order/12`

```json
{
  "order_number": 12,
  "drink": "🧋 Brown Sugar Milk Tea",
  "served_by": "✨ Hanii! ✨"
}
```

### `POST /submit_order`

```json
{
  "name": "Alex",
  "drink": "Strawberry Matcha",
  "topping": "Pearls"
}
```

**Returns:**

```json
{
  "message": "🧋 Order received for Alex!",
  "your_drink": "Strawberry Matcha",
  "topping": "Pearls",
  "served_by": "✨ Hanii! ✨"
}
```

## 💻 How to Run Locally

```bash
git clone https://github.com/Airlles/fastapi-ci-cd.git
cd fastapi-ci-cd
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit:
```
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```

## ✅ Run Tests

```bash
pytest
```

✔️ Tests include:
- GET `/`
- GET `/order/{id}`
- GET `/custom_order/{name}`
- POST `/submit_order`

## 📈 Project Status

This project is complete and deployed. Future ideas:
- Add topping validation
- Add SQLite DB to store orders
- Rate limiting or authentication
- HTML frontend for real use

## 👤 Maintainer

**Hani Ahmed**  
GitHub: [Airlles](https://github.com/Airlles)  
Built as a showcase for backend engineering skills using modern Python tooling.
