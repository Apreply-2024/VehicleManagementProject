from fastapi import APIRouter
from typing import List
from schemas.user_schema import UserLogin
from schemas.response_schema import APIResponse
from schemas.user_schema import (
    UserCreate,
    UserResponse
)

from schemas.user_schema import (
    UserCreate,
    UserResponse,
    UserLogin,
    TokenResponse
)

from services import user_service


router = APIRouter(
    prefix="/api/v1",
    tags=["Users"]
)


@router.post(
    "/users",
    response_model=APIResponse[UserResponse],
    summary="Create user",
    description="Register a new user."
)
def create_user(user: UserCreate):

    return user_service.create_user_service(user)

@router.get(
    "/users",
    response_model=APIResponse[List[UserResponse]]
)
def get_users():

    return user_service.get_all_users_service()

@router.get(
    "/users/{user_id}",
    response_model=APIResponse[UserResponse]
)
def get_user(user_id: int):

    return user_service.get_user_service(user_id)

@router.put(
    "/users/{user_id}",
    response_model=APIResponse[UserResponse]
)
def update_user(
        user_id: int,
        user: UserCreate
):

    return user_service.update_user_service(
        user_id,
        user
    )

@router.delete(
    "/users/{user_id}",
    response_model=APIResponse[UserResponse]
)
def delete_user(user_id: int):

    return user_service.delete_user_service(
        user_id
    )

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(user: UserLogin):

    return user_service.login_service(user)

@router.post(
    "/users/login",
    summary="User login",
    description="Authenticate user credentials."
)
def login_user(
        user_credentials: UserLogin
):

    return user_service.login_user_service(
        user_credentials
    )