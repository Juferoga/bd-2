from pydantic import BaseModel

class Region(BaseModel):
    id: str
    nombre: str
