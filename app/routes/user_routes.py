from fastapi import APIRouter
from app.models.user import User
from app.core.database import SessionLocal

user_router = APIRouter(prefix="/user_router")
session = SessionLocal()


@user_router.get('/all_users')
def get_all_users():
    return session.query(User).all()

@user_router.get('/get_user/{id_user}')
def get_user_id():
    return 'get user_router for id'

@user_router.post('/create_user')
def crate_user():
    return 'create new user_router in db'

@user_router.put('/update_user/{id_user}')
def update_user():
    return 'update user_router un db'

@user_router.delete('/delete_user/{id_user}')
def delete_user():
    return 'delete user un db'