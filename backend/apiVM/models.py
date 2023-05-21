from pydantic import BaseModel

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