import json
import codecs
from configuration import database
from datetime import date, timedelta
from sqlalchemy import create_engine

banco = 'dbContabil'
tb_banco = 'cadplano'

class MySqlQuery():
    def execute(self,db,query):
        # Define os dados do banco
        database_settings = database.Settings()

        # Set database to query
        database_settings.setDatabase(db)

        str_conn = '''mysql://{0}:{1}@{2}:{3}/{4}
            '''.format(database_settings.user(),
                       database_settings.password(),
                       database_settings.host(),
                       database_settings.port(),
                       database_settings.database()
                       )

        try:
            engine  = create_engine(str_conn)
            conexao = engine.connect()
            result = conexao.execute(query)
            return result

        finally:
            conexao.close()

    def get_registro(self, id):
        if (id == '0'):
            query = 'select * from {0}.{1}'.format(banco, tb_banco)
        else:
            query = 'select * from {0}.{1} where idplano = {2}'.format(banco, tb_banco, int(id))

        result = []

        data = self.execute(banco, query)

        rows = data.fetchall()

        for row in rows:
            result.append({
                "idplano": row['idplano'],
                "codigo": row['codigo'],
                "descricao": row['descricao'].decode('latin1'),
                "tipocd": row['tipocd'],
                "grupoplano": row['grupoplano']
            })   

        retorno = {'cadplano': result}
        return retorno

    def cria_registro(self, data):

        reg = json.loads(data)

        novo = self.proximo_codigo()

        query = 'insert into ' + banco + '.' + tb_banco + ' (idplano, codigo, descricao, tipocd, grupoplano) values (' + str(novo) + ',"' + str(reg['codigo']) + '","' + reg['descricao'] + '","' + reg['tipocd'] + '","' + reg['grupoplano'] + '")'                                            

#        print query
#        query = 'insert into {0}.{1}(idplano, codigo, descricao, tipocd) values ({2}, {3}, "{4}", "{5}")'.format(banco, tb_banco, 
#            novo, 
#            reg['codigo'], 
#            nome.encode('ascii', 'ignore'), #.decode('utf-8'), 
#            reg['descricao'],
#            reg['tipocd']
#            )

        retorno = self.execute(banco, query)

    def proximo_codigo(self):
        query = 'select max(idplano) from {0}.{1}'.format(banco, tb_banco)

        prox = 0
        retorno = self.execute(banco, query).fetchone()

        for value in retorno:
            prox = value

        if  prox == None:
            prox = 0

        prox = prox + 1
        return prox

    def deleta_registro(self, data):
        query = 'delete from {0}.{1} where idplano = {2}'.format(banco, tb_banco, int(data) )
        retorno = self.execute(banco, query)

    def altera_registro(self, data):
        reg = json.loads(data)

        query = 'update ' + banco + '.' + tb_banco + ' set codigo="' + reg['codigo'] + '", descricao="' + reg['descricao'] + '", tipocd="' + reg['tipocd'] + '", grupoplano="' + reg['grupoplano'] + '" where idplano = ' + str(reg['idplano'])

        # query = 'update {0}.{1} set codigo = {3}, descricao = "{4}", tipocd="{5}" where idplano = {2}'.format(banco, tb_banco, 
        #      reg['idplano'],
        #      reg['codigo'],
        #      reg['descricao'].encode('latin1'),
        #      reg['tipocd']
        #      )

        retorno = self.execute(banco, query)
