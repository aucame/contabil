import simplejson as json
import codecs
from configuration import database
from datetime import date, timedelta
from sqlalchemy import create_engine

banco = 'dbContabil'
tb_banco = 'cadlancamento'

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
            query = 'select * from {0}.{1} where idlancamento = {2}'.format(banco, tb_banco, int(id))

        result = []

        data = self.execute(banco, query)

#        for v in data:
#            print(v)

#            for column, value in v.items():
#                a = column
#                b = json.dumps(value)
#                c = {a:b}
#                print(c)
#                result.append(c)

#                result.append({column: value})

#                result.append({'{0}: {1}'.format(column, value)})

        for value in data:
            result.append({
                'idlancamento': value['idlancamento'], 
                'ano': value['ano'], 
                'mes': value['mes'],
                'idplano': value['idplano'],
                'valor': json.dumps(value['valor'])
#                'valor': value['valor']
                })
    
        retorno = {'cadlancamento': result}
        return retorno

    def cria_registro(self, data):
        reg = json.loads(data)

        novo = self.proximo_codigo()

        query = 'insert into {0}.{1}(idlancamento, ano, mes, idplano, valor) values ({2}, {3}, {4}, {5}, {6})'.format(banco, tb_banco, 
            novo, 
            reg['ano'], 
            reg['mes'], 
            reg['idplano'],
            reg['valor']
            )

        retorno = self.execute(banco, query)

    def proximo_codigo(self):
        query = 'select max(idlancamento) from {0}.{1}'.format(banco, tb_banco)

        prox = 0
        retorno = self.execute(banco, query).fetchone()

        for value in retorno:
            prox = value

        if  prox == None:
            prox = 0

        prox = prox + 1
        return prox

    def deleta_registro(self, data):
        query = 'delete from {0}.{1} where idlancamento = {2}'.format(banco, tb_banco, 
            int(data)
            )
        retorno = self.execute(banco, query)

    def altera_registro(self, data):
        reg = json.loads(data)
        query = 'update {0}.{1} set ano = {3}, mes = {4}, idplano="{5}", valor={6} where idlancamento = {2}'.format(banco, tb_banco, 
            reg['idlancamento'],
            reg['ano'],
            reg['mes'],
            reg['idplano'],
            reg['valor']
            )
        retorno = self.execute(banco, query)
