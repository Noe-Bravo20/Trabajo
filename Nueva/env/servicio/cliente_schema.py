from pydantic import BaseModel
from typing import Optional
class ClienteSchema(BaseModel):
    id: Optional[str]
    nombre: str
    apellido: str
    usuario: str
    contraseña: str

class DataCliente(BaseModel):
    usuario: str
    contraseña: str