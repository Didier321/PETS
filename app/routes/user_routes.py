from fastapi import APIRouter
from app.models.user import User
from app.core.database import SessionLocal
from app.schemas.userSchema import UserBase


user_router = APIRouter(prefix="/user_router")
session = SessionLocal()


@user_router.get('/all_users')
def get_all_users():
    return session.query(User).all()

@user_router.get('/get_user/{id_user}')
def get_user_id(id_user:int):
   return session.get(User,id_user)

@user_router.post('/create_user')
def crate_user(user : UserBase):
    new_user = User(**user.dict()) 
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return user

@user_router.put('/update_user/{id_user}')
def update_user(id_user:int, userUpdate: UserBase):
    consultaUser = session.get(User, id_user)
    if consultaUser:
        consultaUser.name = userUpdate.name
        consultaUser.email = userUpdate.email
        consultaUser.is_active = userUpdate.is_active
        session.commit()
        session.refresh(consultaUser)
        return consultaUser
    return "User not foud"


@user_router.delete('/delete_user/{id_user}')
def delete_user(id_use : int):
    userDelete= session.get(User,id_use)
    if userDelete:
        session.delete(userDelete)
        session.commit()
        return "user deleted "
    return "user not found"