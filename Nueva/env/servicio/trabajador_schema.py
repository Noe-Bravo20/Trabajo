from pydantic import BaseModel
from typing import Optional

class TrabajadorSchema(BaseModel):
    id: Optional[str]
    nombre: str
    apellido: str
    telefono: str