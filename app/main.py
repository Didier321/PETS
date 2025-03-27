from fastapi import FastAPI
from app.models import user
from app.routes.user_routes import user_router as userRouter
from app.core.database import Base, engine

app = FastAPI()



    
user.Base.metadata.create_all(bind=engine)
app.include_router(userRouter)
@app.get('/')
def root():
    return 'Hola a todos'
