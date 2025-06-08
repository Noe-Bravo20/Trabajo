from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from servicio.empresa_schema import EmpresaSchema
from config.db import engine
from modelo.empresa import empresa
from typing import List
import doctest

empresa= APIRouter()

@empresa.post("/api/empresa", status_code=HTTP_201_CREATED)
def create_empresa(data_empresa: EmpresaSchema):
    
    #"""
    #ingresa los datos de empresa
    #>>>
    create_empresa("1","coca-cola")
    #"""
    with engine.connect() as conn:
    
        new_empresa = data_empresa.dict()    
        conn.execute(empresa.insert().values(new_empresa))
        return Response(status_code=HTTP_201_CREATED)

if __name__ == "__main__":
    doctest.testmod()    

@empresa.put("/api/empresa/{empresa_id}", response_model=EmpresaSchema)
def update_empresa(data_update: EmpresaSchema, empresa_id: str):
    #"""
    #los datos se actualiza 
    #>>>
    update_empresa("1","pepsi")
    #"""
    with engine.connect() as conn:
        conn.execute(empresa.update().values(nombre=data_update.nombre))

        result = conn.execute(empresa.select().where(empresa.c.id == empresa_id)).first()

        return result
    

@empresa.delete("/api/empresa/{empresa_id}", status_code=HTTP_204_NO_CONTENT)
def delete_empresa(empresa_id: str):
    #"""
    #elimina todos los datos 
    #>>>
    delete_empresa("","")
    #"""
    with engine.connect() as conn:
        conn.execute(empresa.delete().where(empresa.c.id == empresa_id))

        return Response(status_code=HTTP_204_NO_CONTENT)