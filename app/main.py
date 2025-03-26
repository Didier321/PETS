from fastapi import FastAPI
from app.models import user

from app.core.database import Base, engine

app = FastAPI()


    
user.Base.metadata.create_all(bind=engine)

@app.get('/')
def root():
    return 'Hola a todos'

@app.get('/all_users')
def get_all_users():
    return "all users"


@app.get('/get_user/{id_user}')
def get_user_id():
    return 'get user for id'

@app.post('/create_user')
def crate_user():
    return 'create new user in db'

@app.put('/update_user/{id_user}')
def update_user():
    return 'update user un db'

@app.delete('/delete_user/{id_user}')
def delete_user():
    return 'delete user un db'