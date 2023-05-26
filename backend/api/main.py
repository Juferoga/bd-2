from fastapi import FastAPI
from dotenv import load_dotenv
from routes.auth import auth_routes
from routes.user import user_routes
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



app = FastAPI()
app.include_router(auth_routes, prefix='/api')
app.include_router(user_routes, prefix='/api')
load_dotenv()
