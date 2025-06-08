from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, Date, Time, CHAR
from config.db import engine, meta

pedido = Table("pedido", meta,
              Column("id",Integer, primary_key=True),
              Column("Detalle", Date, nullable=False))


meta.create_all(engine)