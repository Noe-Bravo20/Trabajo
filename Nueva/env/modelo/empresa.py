from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta

empresa = Table("empresa", meta,
              Column("ruc",Integer, primary_key=True),
              Column("Nombre", String(255), nullable=False))
              
  
meta.create_all(engine)