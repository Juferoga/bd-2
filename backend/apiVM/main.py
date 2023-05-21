from fastapi import FastAPI, Response
from typing import Union
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from connect import Connect

app = FastAPI()

global con
con = None

origins = [
    "http://127.0.0.1:5500",
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

class Usuario(BaseModel):
    k_usuario: int
    t_nombre: str
    t_apellido: str
    f_nacimiento: str
    i_genero: str
    n_telefono: int
    t_direccion: str
    t_email: str
    i_estado: str

class Representante(BaseModel):
    k_representante: int
    f_contrato: str
    k_region: str
    k_pais: str
    k_clasificacion: str
    k_jefe: int

class Cliente(BaseModel):
    k_cliente: int
    t_ciudad: str
    k_representante: int

@app.post("/login")
def login(login:Login, r:Response):
    global con
    con = Connect(login.user, login.password)
    res = con.open_connection()
    response["message"] = res[1]
    if res[0]:
        response["data"] = {"user": login.user}
        response["status"] = 200
    else:
        r.status_code = 400
        response["status"] = 400
        con = None
    print(response)
    return response

@app.get("/logout")
def logout(r:Response):
    global con
    print(con)
    if con != None:
        con.close_connection()
        response["message"] = "Cerrando conexion"
        response["status"] = 200
        con = None
    else:
        r.status_code = 400
        response["message"] = "No hay conexion"
        response["status"] = 400
    return response

@app.post("/representante")
def representante(user:Usuario, rep:Representante, r:Response):
    if con != None:
        res1 = con.execute_query("insert into usuario (k_usuario, t_nombre, t_apellido, f_nacimiento, i_genero, n_telefono, t_direccion, t_email, i_estado) values (:1, :2, :3, to_date(:4, 'YYYY-MM-DD'), :5, :6, :7, :8, :9)", (user.k_usuario, user.t_nombre, user.t_apellido, user.f_nacimiento, user.i_genero, user.n_telefono, user.t_direccion, user.t_email, user.i_estado))
        res2 = con.execute_query("insert into representante (k_representante, f_contrato, k_usuario, k_region, k_pais, k_clasificacion, k_jefe) values (:1, to_date(:2, 'YYYY-MM-DD'), :3, :4, :5, :6, :7)", (rep.k_representante, rep.f_contrato, user.k_usuario, rep.k_region, rep.k_pais, rep.k_clasificacion, rep.k_jefe))
        if res1[0] == False or res2[0] == False:
            r.status_code = 400
            response["message"] = res1[1] if res1[0] == False else res2[1]
            response["status"] = 400
        else:
            con.commit()
            response["message"] = 'Representante creado correctamente'
            response["status"] = 200
    else:
        r.status_code = 401
        response["message"] = "No autenticado"
        response["status"] = 401
    return response

@app.post("/cliente")
def representante(user:Usuario, cli:Cliente, r:Response):
    if con != None:
        res1 = con.execute_query("insert into usuario (k_usuario, t_nombre, t_apellido, f_nacimiento, i_genero, n_telefono, t_direccion, t_email, i_estado) values (:1, :2, :3, to_date(:4, 'YYYY-MM-DD'), :5, :6, :7, :8, :9)", (user.k_usuario, user.t_nombre, user.t_apellido, user.f_nacimiento, user.i_genero, user.n_telefono, user.t_direccion, user.t_email, user.i_estado))
        res2 = con.execute_query("insert into cliente (k_cliente, t_ciudad, k_usuario, k_representante) values (:1, :2, :3, :4)", (cli.k_cliente, cli.t_ciudad, user.k_usuario, cli.k_representante))
        if res1[0] == False or res2[0] == False:
            r.status_code = 400
            response["message"] = res1[1] if res1[0] == False else res2[1]
            response["status"] = 400
        else:
            con.commit()
            response["message"] = 'Cliente creado correctamente'
            response["status"] = 200
    else:
        r.status_code = 401
        response["message"] = "No autenticado"
        response["status"] = 401
    return response