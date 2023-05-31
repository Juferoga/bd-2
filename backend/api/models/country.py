from pydantic import BaseModel

class Country(BaseModel):
    id: str
    nombre: str