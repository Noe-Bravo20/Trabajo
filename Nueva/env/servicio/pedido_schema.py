from pydantic import BaseModel
from typing import Optional
class PedidoSchema(BaseModel):
    id: Optional[str]
    Detalle: str
