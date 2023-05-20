from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from connect import Connect

app = FastAPI()

global con
con = None

origins = [
    "http://127.0.0.2:5500",
]

response = {
    "message": "",
    "data": {},
    "status": 0
}

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class Login(BaseModel):
    user: str
    password: str

@app.post("/login")
def login(login:Login):
    global con
    con = Connect(login.user, login.password)
    res = con.open_connection()
    response["message"] = res[1]
    if res[0]:
        response["data"] = {"user": login.user, "password": login.password}
        response["status"] = 200
    else:
        response["status"] = 400
    print(response)
    return response

@app.get("/logout")
def logout():
    global con
    print(con)
    if con != None:
        con.close_connection()
        response["message"] = "Cerrando conexion"
        response["status"] = 200
    else:
        response["message"] = "No hay conexion"
        response["status"] = 400
    return response
