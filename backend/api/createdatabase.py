
from sqlalchemy import *
from configuration import database

dba = 'dbContabil'

database_settings = database.Settings()
database_settings.setDatabase(dba)

usuario  = database_settings.user()
senha    = database_settings.password()
servidor = database_settings.host()
porta    = database_settings.port()
database = database_settings.database()

strconn = "mysql://{0}:{1}@{2}:{3}/{4}".format(usuario, senha, servidor, porta, database)

db = create_engine(strconn)
db.echo = False  # Try changing this to True and see what happens
metadata = MetaData(db)

cadcliente = Table('cadclientes', metadata,
    Column('idcliente', Integer, primary_key=True),
    Column('nome', String(40)),
    Column('endereco', String(40)),
    Column('fonecomercial', String(40)),
    Column('foneresidencial', String(40)),
    schema='dbContabil'
)

cadcliente.create()
