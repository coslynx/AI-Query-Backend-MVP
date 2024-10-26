from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from api.schemas import Token, User
from api.utils import create_access_token, get_user, verify_password
from sqlalchemy.orm import Session

# Import Statements
# 1. Core Modules
from typing import Optional
# 2. Third-Party Libraries
from fastapi.responses import JSONResponse
# 3. Internal Modules
from api.database import get_db

# Environment Variables
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")  # JWT Secret Key

# Router Definition
auth_router = APIRouter()

# API Endpoint for Authenticating Users and Generating JWT Tokens
@auth_router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Authenticates a user based on username and password, and generates a JWT access token.

    Args:
        form_data (OAuth2PasswordRequestForm): The user's credentials, including username and password.
        db (Session): The database session for retrieving user information.

    Returns:
        JSONResponse: A JSON response containing the JWT access token.
    """
    user = get_user(form_data.username, db)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return JSONResponse(
        content={"access_token": access_token, "token_type": "bearer"}
    )