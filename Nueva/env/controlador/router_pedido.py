from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from servicio.pedido_schema import PedidoSchema
from config.db import engine
from modelo.pedido import pedido
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
import doctest

pedido= APIRouter()


@pedido.post("/api/pedido", status_code=HTTP_201_CREATED)
def create_pedido(data_pedido: PedidoSchema):
    #"""
    #los usuarios ingresa los pedido
    #>>> 
    create_pedido("1","pedidoooo")
    #"""
    with engine.connect() as conn:
    
        new_pedido = data_pedido.dict()
    
        conn.execute(pedido.insert().values(new_pedido))

        return Response(status_code=HTTP_201_CREATED)
if __name__ == "__main__":
    doctest.testmod() 

@pedido.put("/api/pedido/{pedido_id}", response_model=PedidoSchema)
def update_pedido(data_update: PedidoSchema, pedido_id: str):
    #"""
    #la informacion del pedido
    #>>>
    update_pedido("2","inf pedido")
    #"""
    with engine.connect() as conn:
        conn.execute(pedido.update().values(detalle=data_update.detalle))

        result = conn.execute(pedido.select().where(pedido.c.id == pedido_id)).first()

        return result
    

@pedido.delete("/api/pedido/{pedido_id}", status_code=HTTP_204_NO_CONTENT)
def delete_pedido(pedido_id: str):
    #"""
    #elimina los pedidos
    #>>>
    delete_pedido("","")
    #"""
    with engine.connect() as conn:
        conn.execute(pedido.delete().where(pedido.c.id == pedido_id))

        return Response(status_code=HTTP_204_NO_CONTENT)