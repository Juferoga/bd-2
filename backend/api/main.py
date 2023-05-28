from fastapi import FastAPI
from dotenv import load_dotenv
from routes.auth import auth_routes
from routes.user import user_routes
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_routes, prefix='/api')
app.include_router(user_routes, prefix='/api')
load_dotenv()
