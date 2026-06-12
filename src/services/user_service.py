from schemas.response_schema import APIResponse
from utils.security import hash_password
from schemas.user_schema import UserLogin
from utils.security import verify_password
from schemas.user_schema import (
    UserCreate,
    UserResponse
)

from exceptions.custom_exceptions import AppException

from repositories.user_repository import (
    create_user,
    get_user_by_email,
    get_user_by_username,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)

def create_user_service(user: UserCreate):

    existing_email = get_user_by_email(user.email)
    if existing_email:
        raise AppException("Email already exists", 400)

    existing_username = get_user_by_username(user.username)
    if existing_username:
        raise AppException("Username already exists", 400)

    hashed_password = hash_password(user.password)

    user.password = hashed_password

    db_user = create_user(user)

    return APIResponse(
        success=True,
        message="User created successfully",
        data=db_user
    )

def get_all_users_service():

    users = get_all_users()

    return APIResponse(
        success=True,
        message="Users fetched successfully",
        data=users
    )

def get_user_service(user_id: int):

    user = get_user_by_id(user_id)

    if not user:
        raise AppException(
            "User not found",
            404
        )

    return APIResponse(
        success=True,
        message="User fetched successfully",
        data=user
    )

def update_user_service(
        user_id: int,
        user: UserCreate
):

    updated_user = update_user(
        user_id,
        user
    )

    if not updated_user:
        raise AppException(
            "User not found",
            404
        )

    return APIResponse(
        success=True,
        message="User updated successfully",
        data=updated_user
    )

def delete_user_service(user_id: int):

    deleted_user = delete_user(user_id)

    if not deleted_user:
        raise AppException(
            "User not found",
            404
        )

    return APIResponse(
        success=True,
        message="User deleted successfully",
        data=deleted_user
    )


def login_user_service(
        user_credentials: UserLogin
):

    user = get_user_by_email(
        user_credentials.email
    )

    if not user:
        raise AppException(
            "Invalid email or password",
            401
        )

    if not verify_password(
            user_credentials.password,
            user.password
    ):

        raise AppException(
            "Invalid email or password",
            401
        )

    return APIResponse(
        success=True,
        message="Login successful",
        data={
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        }
    )

