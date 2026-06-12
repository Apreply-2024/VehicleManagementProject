from database.database import SessionLocal
from models.user_model import UserModel
from database.database import SessionLocal
from utils.security import verify_password
from utils.auth import create_access_token
from exceptions.custom_exceptions import AppException

def create_user(user):

    db = SessionLocal()

    db_user = UserModel(
        username=user.username,
        email=user.email,
        password=user.password,
        role=user.role
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    db.close()

    return db_user


def get_user_by_email(email: str):

    db = SessionLocal()

    user = (
        db.query(UserModel)
        .filter(UserModel.email == email)
        .first()
    )

    db.close()

    return user


def get_user_by_username(username: str):

    db = SessionLocal()

    user = (
        db.query(UserModel)
        .filter(UserModel.username == username)
        .first()
    )

    db.close()

    return user

def get_all_users():

    db = SessionLocal()

    users = db.query(UserModel).all()

    db.close()

    return users

def get_user_by_id(user_id: int):

    db = SessionLocal()

    user = (
        db.query(UserModel)
        .filter(UserModel.id == user_id)
        .first()
    )

    db.close()

    return user

def update_user(user_id: int, user):

    db = SessionLocal()

    db_user = (
        db.query(UserModel)
        .filter(UserModel.id == user_id)
        .first()
    )

    if not db_user:
        db.close()
        return None

    db_user.username = user.username
    db_user.email = user.email
    db_user.password = user.password
    db_user.role = user.role

    db.commit()
    db.refresh(db_user)

    db.close()

    return db_user

def delete_user(user_id: int):

    db = SessionLocal()

    db_user = (
        db.query(UserModel)
        .filter(UserModel.id == user_id)
        .first()
    )

    if not db_user:
        db.close()
        return None

    db.delete(db_user)

    db.commit()

    db.close()

    return db_user


def login_service(user_login):

    user = get_user_by_email(
        user_login.email
    )

    if not user:
        raise AppException(
            "Invalid credentials",
            401
        )

    if not verify_password(
            user_login.password,
            user.password
    ):
        raise AppException(
            "Invalid credentials",
            401
        )

    token = create_access_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


