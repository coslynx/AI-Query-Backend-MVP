from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from api.routers import query_router, auth_router
from api.database import engine, Base
from api.utils import get_db
from api.schemas import Token

# 1. Core Modules
from typing import Union
from datetime import datetime

# 2. Third-Party Libraries
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

# 3. Internal Modules
from .schemas import Token
from .utils import create_access_token

# Environment Variables
JWT_SECRET_KEY = "your_secret_key"  # Replace with a strong, unique secret key

# Initialize FastAPI Application
app = FastAPI()

# Set up CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for your specific needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(query_router)
app.include_router(auth_router)

# Database Initialization
@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)