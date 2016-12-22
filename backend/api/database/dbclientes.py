import json
import codecs
from configuration import database
from datetime import date, timedelta
from sqlalchemy import create_engine

banco = 'dbContabil'
tb_tabela = 'cadclientes'

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

    def get_clientes(self, id):
        if (id == '0'):
            query = 'select * from {0}.{1}'.format(banco, tb_tabela)
        else:
            query = 'select * from {0}.{1} where idcliente = {2}'.format(banco, tb_tabela, int(id))

        result = []

        data = self.execute(banco, query)
        for value in data:
            result.append({
                'idcliente': value['idcliente'], 
                'nome': value['nome'].decode('latin1'), 
                'endereco': value['endereco'].decode('latin1'),
                'fonecomercial': value['fonecomercial'],
                'foneresidencial': value['foneresidencial']
                })
    
        retorno = {'cadclientes': result}
        return retorno

    def cria_cliente(self, data):
        reg = json.loads(data)

        idcliente = self.proximo_codigo()

        query = 'insert into ' + banco + '.' + tb_tabela + ' (idcliente, nome, endereco, fonecomercial, foneresidencial) values (' + str(idcliente) + ',"' + reg['nome'] + '","' + reg['endereco'] + '","' + reg['fonecomercial'] + '","' + reg['foneresidencial'] + '")'

        # print query

        # query = 'insert into {0}.{1}(idcliente, nome, endereco, fonecomercial, foneresidencial) values ({2}, "{3}", "{4}", "{5}", "{6}")'.format(banco, tb_tabela, 
        #     idcliente, 
        #     reg['nome'], 
        #     reg['endereco'], 
        #     reg['fonecomercial'],
        #     reg['foneresidencial']
        #     )

        retorno = self.execute(banco, query)

    def proximo_codigo(self):
        query = 'select max(idcliente) from {0}.{1}'.format(banco, tb_tabela)

        prox = 0
        retorno = self.execute(banco, query).fetchone()

        for value in retorno:
            prox = value

        if  prox == None:
            prox = 0

        prox = prox + 1
        return prox

    def deleta_cliente(self, data):
        query = 'delete from {0}.{1} where idcliente = {2}'.format(banco, tb_tabela, 
            int(data)
            )
        retorno = self.execute(banco, query)

    def altera_cliente(self, data):
        reg = json.loads(data)

        query = 'update ' + banco + '.' + tb_tabela + ' set nome="' + reg['nome'] + '", endereco="' + reg['endereco'] + '", fonecomercial="' + reg['fonecomercial'] + '", foneresidencial="' + reg['foneresidencial'] + '", where idcliente = ' + str(reg['idcliente'])

        # query = 'update {0}.{1} set nome = "{2}", endereco = "{4}", fonecomercial="{5}", foneresidencial="{6}" where idcliente = {3}'.format(banco, tb_tabela, 
        #     reg['nome'],
        #     reg['idcliente'],
        #     reg['endereco'],
        #     reg['fonecomercial'],
        #     reg['foneresidencial']
        #     ) 
        retorno = self.execute(banco, query)
