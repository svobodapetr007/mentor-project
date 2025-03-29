from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models import models
from schemas import schemas
from utils.auth import get_password_hash, verify_password

def get_user_by_username(db: Session, username: str):
    """Get a user by username"""
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    """Get a user by email"""
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    """Create a new user"""
    # Check if username exists
    db_username = get_user_by_username(db, username=user.username)
    if db_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    # Check if email exists
    db_email = get_user_by_email(db, email=user.email)
    if db_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_active=True
    )
    
    # Add to database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    """Authenticate a user with username and password"""
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user