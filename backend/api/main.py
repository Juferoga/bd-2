from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes.auth import auth_routes
from routes.user import user_routes
from routes.represantes import representantes_routes
from routes.product import product_routes
from routes.client import client_routes
from routes.country import country_routes
from routes.region import region_routes
from routes.classification import classification_routes
from routes.orders import order_routes
from routes.ware_house import warehouse_routes
from routes.statics import statics_routes


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
app.include_router(representantes_routes, prefix='/api')
app.include_router(client_routes, prefix='/api')
app.include_router(product_routes, prefix='/api')
app.include_router(country_routes, prefix='/api')
app.include_router(region_routes, prefix='/api')
app.include_router(classification_routes, prefix='/api')
app.include_router(order_routes, prefix='/api')
app.include_router(warehouse_routes, prefix='/api')
app.include_router(statics_routes, prefix='/api')
load_dotenv()
