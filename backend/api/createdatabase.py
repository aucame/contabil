
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
        Column('meddiafat', Integer),
        Column('paramostra', Integer),
        schema=dba
    )

    cadparam.create()

def cria_Plano():

    cadplano = Table('cadplano', metadata,
        Column('idplano', Integer, primary_key=True),
        Column('codigo', String(20)),
        Column('descricao', String(100)),
        Column('tipocd', String(1)),
        Column('tipo', Numeric(2,0)),
        Column('grupo', Numeric(2,0)),
        Column('subgrupo', Numeric(2,0)),
        Column('subgrp', Numeric(3,0)),
        Column('numero', Numeric(5,0)),
        Column('grupoplano', String(50)),
        schema=dba
    )

    cadplano.create()

def cria_Lancamento():

    cadlancamento = Table('cadlancamento', metadata,
        Column('idlancamento', Integer, primary_key=True),
        Column('ano', Integer),
        Column('mes', Integer),
        Column('idplano', String(20)),
        Column('valor', Numeric(8,2)),
        Column('idcliente', Integer)
        schema=dba
    )

    cadlancamento.create()

#cria_Usuario()
#cria_Cliente()
#cria_Empresa()
#cria_Parametro()
#cria_Plano()
#cria_Lancamento()
