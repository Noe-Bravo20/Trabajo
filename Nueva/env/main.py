from typing import Union
from controlador.router import cliente
from fastapi import FastAPI
from controlador.router_trabajador import trabajador
from controlador.router_pedido import pedido
from controlador.router_empresa import empresa

app = FastAPI()

app.include_router(cliente)

app.include_router(trabajador)

app.include_router(pedido)

app.include_router(empresa)
