import simplejson as json
import codecs
from configuration import database
from datetime import date, timedelta
from sqlalchemy import create_engine

banco = 'dbContabil'
tb_banco = 'cadparam'

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
                       database_settings.database())

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
            query = 'select * from {0}.{1} where idparam = {2}'.format(banco, tb_banco, int(id))

        result = []

        data = self.execute(banco, query)

        for value in data:
            result.append({
                'idparam': value['idparam'], 
                'mes': value['mes'], 
                'ano': value['ano'],
                'idempresa': value['idempresa'],
                'diasuteis': value['diasuteis'],
                'meddiafat': value['meddiafat'],
                'paramostra': value['paramostra'],
                'fatamostra': json.dumps(value['fatamostra'])
                })
    
        retorno = {'cadparam': result}
        return retorno

    def cria_registro(self, data):
        reg = json.loads(data)

        novo = self.proximo_codigo()

        query = 'insert into {0}.{1}(idparam, mes, ano, idempresa, diasuteis, meddiafat, paramostra, fatamostra) values ({2}, {3}, {4}, {5}, {6}, {7}, {8}, {9})'.format(banco, tb_banco, 
            novo, 
            reg['mes'], 
            reg['ano'], 
            reg['idempresa'],
            reg['diasuteis'],
            reg['meddiafat'],
            reg['paramostra'],
            reg['fatamostra']
            )

        retorno = self.execute(banco, query)

    def proximo_codigo(self):
        query = 'select max(idparam) from {0}.{1}'.format(banco, tb_banco)

        prox = 0
        retorno = self.execute(banco, query).fetchone()

        for value in retorno:
            prox = value

        if  prox == None:
            prox = 0

        prox = prox + 1
        return prox

    def deleta_registro(self, data):
        query = 'delete from {0}.{1} where idparam = {2}'.format(banco, tb_banco, 
            int(data)
            )
        retorno = self.execute(banco, query)

    def altera_registro(self, data):
        reg = json.loads(data)
        query = 'update {0}.{1} set mes = {3}, ano = {4}, idempresa={5}, diasuteis={6}, meddiafat={7}, paramostra={8}, fatamostra={9} where idparam = {2}'.format(banco, tb_banco, 
            reg['idparam'],
            reg['mes'],
            reg['ano'],
            reg['idempresa'],
            reg['diasuteis'],
            reg['meddiafat'],
            reg['paramostra'],
            reg['fatamostra']
            )
        retorno = self.execute(banco, query)
