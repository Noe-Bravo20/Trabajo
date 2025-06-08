from pydantic import BaseModel
from typing import Optional
class EmpresaSchema(BaseModel):
    id: Optional[str]
    Nombre: str