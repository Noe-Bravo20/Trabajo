from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from servicio.trabajador_schema import TrabajadorSchema
from config.db import engine
from modelo.trabajador import trabajador
#from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
import doctest

trabajador= APIRouter()

@trabajador.get("/")
def root():
    return{ "enni"}

@trabajador.get("/api/trabajador", response_model=List[TrabajadorSchema])
def get_trabajador():
    with engine.connect() as conn:
        result = conn.execute(trabajador.select()).fetchall()
        return result
    
@trabajador.get("/api/trabajador/{trabajador_id}", response_model=TrabajadorSchema)
def get_trabajador(trabajador_id:str):
    with engine.connect() as conn:
        result = conn.execute(trabajador.select().where(trabajador.c.id == trabajador_id)).first()

        return result

@trabajador.post("/api/trabajador", status_code=HTTP_201_CREATED)
def create_Trabajador(data_trabajador: TrabajadorSchema):
    #"""
    #ingresa los datos de los trabajadores a la base de datos 
    #>>> 
    create_trabajador("1","andres","carpio","1234678")
    #"""
    with engine.connect() as conn:
    
        new_trabajador = data_trabajador.dict()    
        conn.execute(trabajador.insert().values(new_trabajador))

        return Response(status_code=HTTP_201_CREATED)
if __name__ == "__main__":
    doctest.testmod()   

@trabajador.put("/api/trabajador/{trabajador_id}", response_model=TrabajadorSchema)
def update_trabajador(data_update: TrabajadorSchema, trabajador_id: str):
    #"""
    #los datos de los usuario o trabajador se actualiza si desea actualizar
    #>>>
    update_trabajador("1","Javir","Perez","1239999")
    #"""
    with engine.connect() as conn:
        conn.execute(trabajador.update().values(nombre=data_update.nombre, 
        apellido=data_update.apellido, telefono=data_update.telefono))

        result = conn.execute(trabajador.select().where(trabajador.c.id == trabajador_id)).first()

        return result
    

@trabajador.delete("/api/trabajador/{trabajador_id}", status_code=HTTP_204_NO_CONTENT)
def delete_trabajador(trabajador_id: str):
    #"""
    #elimina todos los datos de un usuraio o trabajador
    #>>>
    delete_trabajador("","","","")
    #"""
    with engine.connect() as conn:
        conn.execute(trabajador.delete().where(trabajador.c.id == trabajador_id))

        return Response(status_code=HTTP_204_NO_CONTENT)