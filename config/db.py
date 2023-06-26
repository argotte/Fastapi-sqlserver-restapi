from sqlalchemy import create_engine
import pymssql
from sqlalchemy.sql.schema import MetaData
SERVER='SERVERNAME'
user='USERNAME'
password='PASSWORD'

engine = create_engine(
    r"mssql+pymssql://{0}:{1}@DIEGUITO/DBNAME?charset=utf8".format(user, password))

meta = MetaData()

conn = engine.connect()