
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

def cria_Usuario():

    cadusuarios = Table('cadusuarios', metadata,
        Column('idusuario', Integer, primary_key=True),
        Column('nome', String(100)),
        Column('login', String(20)),
        Column('ativo', String(3)),
        Column('login', String(20)),
        schema=dba
    )

    cadusuarios.create()

def cria_Cliente():

    cadcliente = Table('cadclientes', metadata,
        Column('idcliente', Integer, primary_key=True),
        Column('nome', String(100)),
        Column('endereco', String(50)),
        Column('fonecomercial', String(20)),
        Column('foneresidencial', String(20)),
        schema=dba
    )

    cadcliente.create()

def cria_Empresa():

    cadempresa = Table('cadempresa', metadata,
        Column('idempresa', Integer, primary_key=True),
        Column('nome', String(100)),
        Column('endereco', String(50)),
        Column('fonecomercial', String(20)),
        schema=dba
    )

    cadempresa.create()

def cria_Parametro():

    cadparam = Table('cadparam', metadata,
        Column('idparam', Integer, primary_key=True),
        Column('mes', Integer),
        Column('ano', Integer),
        Column('idempresa', Integer),
        Column('diasuteis', Integer),
        schema=dba
    )

    cadparam.create()

#cria_Usuario()
#cria_Cliente()
#cria_Empresa()
cria_Parametro()
