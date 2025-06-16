
# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# --- CORS Configuration ---
# List of allowed origins (React app's URL)
# In development, your React app might run on http://localhost:3000, http://localhost:3001, etc.
# In production, replace this with your actual frontend domain(s)
origins = [
    "http://localhost:3000",  # Example: React dev server
    "http://localhost:3001",  # Another possible React dev server port
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
    # "https://your-react-app.com", # Your production frontend
]

# If you want to allow all origins (less secure, use with caution, especially in production)
# origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Specifies the allowed origins
    allow_credentials=True, # Allows cookies to be included in cross-origin requests
    allow_methods=["*"],    # Allows all methods (GET, POST, PUT, DELETE, etc.) or specify like ["GET", "POST"]
    allow_headers=["*"],    # Allows all headers or specify like ["Content-Type", "Authorization"]
)

# --- Sample Pydantic Model ---
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# --- Sample API Endpoints ---
@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI with CORS!"}

@app.get("/api/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q, "message": "Item retrieved successfully"}

@app.post("/api/items/")
async def create_item(item: Item):
    # In a real app, you'd save this item to a database
    print(f"Received item: {item.dict()}")
    return {"item": item.dict(), "message": "Item created successfully"}

# To run this application:
# 1. Save it as main.py
# 2. Install FastAPI and Uvicorn: pip install fastapi uvicorn
# 3. Run Uvicorn: uvicorn main:app --reload --port 8000