from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from servicio.cliente_schema import ClienteSchema, DataCliente
from config.db import engine
from modelo.cliente import cliente
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
import doctest

cliente= APIRouter()

@cliente.get("/")
def root():
    return{"message:" "enni"}

@cliente.get("/api/cliente", response_model=List[ClienteSchema])
def get_cliente():
    with engine.connect() as conn:
        result = conn.execute(cliente.select()).fetchall()
        return result
    
@cliente.get("/api/cliente/{cliente_id}", response_model=ClienteSchema)
def get_cliente(ciente_id:str):
    with engine.connect() as conn:
        result = conn.execute(cliente.select().where(cliente.c.id == cliente_id)).first()

        return result
    

@cliente.post("/api/cliente", status_code=HTTP_201_CREATED)
def create_cliente(data_cliente: ClienteSchema):

    #"""
    #ingresa los usuarios a la base de datos 
    #>>> 
    create_cliente(clienteSchema(id="1", nombre="Enni", apellido="Carreno", usuario="enni", contraseña="123"))

    #"""
    with engine.connect() as conn:
    
        new_cliente = data_cliente.dict()
        new_cliente["contraseña"]= generate_password_hash(data_cliente.contraseña, "pbkdf2:sha256:30", 30)
    
        conn.execute(cliente.insert().values(new_cliente))

        return Response(status_code=HTTP_201_CREATED)

if __name__ == "__main__":
    doctest.testmod()

    
@cliente.post("/api/cliente/login", status_code=200)
def cliente_login(data_cliente: DataCliente):
    #"""
   # verifica el usurairo y contraseña para que ingrese a la pagina corectamente 
    #>>> 
    cliente_login("enni","1234")
    #"""
    with engine.connect() as conn:
        result = conn.execute(cliente.select().where(cliente.c.usuario == data_cliente.usuario)).first()
        if result != None:
            check_passw = check_password_hash(result[3], data_cliente.contraseña)

            if check_passw:
                return {
                    "status": 200,
                    "message": "Access success"
                }
        
        return {
            "status": HTTP_401_UNAUTHORIZED,
            "mensage": "Access denied"
        }
            


@cliente.put("/api/cliente/{cliente_id}", response_model=ClienteSchema)
def update_cliente(data_update: ClienteSchema, cliente_id: str):
    #"""
    #los datos de los usuario o cliente se actualiza si desea actualizar
    #>>>
    update_cliente("1","jorge","rodriguez","vera","12345")
    #"""

    with engine.connect() as conn:
        encryp_contra = generate_password_hash(data_update.contraseña,"pdbkdf2.sha256:30", 30)
        conn.execute(cliente.update().values(nombre=data_update.nombre, 
        apellido=data_update.apellido, usuario=data_update.usuario, contraseña=encryp_contra).where(cleinte.c.id == cliente_id))

        result = conn.execute(cliente.select().where(cliente.c.id == cliente_id)).first()

        return result
    
@cliente.delete("/api/cliente/{cliente_id}", status_code=HTTP_204_NO_CONTENT)
def delete_cliente(cliente_id: str):
    #"""
    #elimina todos los datos 
    #>>>
    delete_cliente("","","","","")
    #"""
    with engine.connect() as conn:
        conn.execute(cliente.delete().where(cliente.c.id == cliente_id))

        return Response(status_code=HTTP_204_NO_CONTENT)
