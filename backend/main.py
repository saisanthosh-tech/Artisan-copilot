# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Import CORS Middleware
from routers import artisan                         # Import your artisan router

# Initialize the FastAPI application
app = FastAPI(
    title="Artisan CoPilot API",
    description="The backend API for the Artisan CoPilot application, powering AI features.",
    version="1.0.0"
)

# --- CORS (Cross-Origin Resource Sharing) Configuration ---
# This is the crucial part that allows your frontend to make requests to this backend.

# Define the list of origins (frontend URLs) that are allowed to connect.
origins = [
    "http://localhost",
    "http://localhost:3000",  # Default for React
    "http://localhost:8080",  # Default for Vue.js
    "http://localhost:4200",  # Default for Angular
    # You can add the URL of your deployed frontend here later
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# --- API Endpoints ---

# Root endpoint to check if the API is running
@app.get("/")
def read_root():
    """
    Root endpoint to confirm the backend is running.
    """
    return {"message": "Artisan CoPilot Backend is running successfully 🚀"}

# Include the router from ./routers/artisan.py
# All endpoints defined in that file will be available under the /artisan prefix.
app.include_router(artisan.router, prefix="/artisan", tags=["Artisan"])