from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import List, Optional
from datetime import datetime

# Database imports are commented out temporarily
# from database.db import get_db, engine
# from models import models
# from schemas import schemas

# models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mentor Project API")

# Configure CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React development server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint to check API status"""
    return {
        "message": "Welcome to Mentor Project API",
        "status": "online",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

# Example endpoint for future use
@app.get("/api/examples")
async def get_examples():
    """Get example data (for demonstration purposes)"""
    return [
        {"id": 1, "name": "Example 1", "description": "This is the first example"},
        {"id": 2, "name": "Example 2", "description": "This is the second example"}
    ]

if __name__ == "__main__":
    # Run the API with uvicorn when the script is executed directly
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)