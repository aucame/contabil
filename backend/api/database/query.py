import json
import codecs
from configuration import database
from datetime import date, timedelta
from sqlalchemy import create_engine

banco = 'dbContabil'
tb_usuarios = 'cadusuarios'

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

    def get_usuarios(self, id):
        if (id == '0'):
            query = 'select * from {0}.{1}'.format(banco, tb_usuarios)
        else:
            query = 'select * from {0}.{1} where idusuarios = {2}'.format(banco, tb_usuarios, int(id))

        result = []

        data = self.execute(banco, query)
        for value in data:
            result.append({
                'idusuario': value['idusuarios'], 
                'nome': value['nome'].decode('latin1'), 
                'ativo': value['ativo'],
                'login': value['login'].decode('latin1')
                })
    
        retorno = {'cadusuarios': result}
        return retorno

    def cria_usuario(self, data):
        reg = json.loads(data)
        novo = self.proximo_codigo()
        query = 'insert into ' + banco + '.' + tb_usuarios + ' (idusuarios, nome, senha, ativo, login) values (' + str(novo) + ',"' + reg['nome'] + '", "' + reg['senha'] + '","' + reg['ativo'] + '","' + reg['login'] + '")'
        retorno = self.execute(banco, query)

        # query = 'insert into {0}.{1}(idusuarios, nome, senha, ativo, login) values ({2}, "{3}", "{4}", "{5}", "{6}")'.format(banco, tb_usuarios, 
        #     novo, 
        #     reg['nome'], 
        #     reg['senha'], 
        #     reg['ativo'],
        #     reg['login']
        #     )


    def proximo_codigo(self):
        query = 'select max(idusuarios) from {0}.{1}'.format(banco, tb_usuarios)

        prox = 0
        retorno = self.execute(banco, query).fetchone()

        for value in retorno:
            prox = value

        if  prox == None:
            prox = 0

        prox = prox + 1
        return prox

    def deleta_usuario(self, data):
        query = 'delete from {0}.{1} where idusuarios = {2}'.format(banco, tb_usuarios, int(data) )
        retorno = self.execute(banco, query)

    def altera_usuario(self, data):
        reg = json.loads(data)
        query = 'update ' + banco + '.' + tb_usuarios + ' set nome = "' + reg['nome'] + '", ativo = "' + reg['ativo'] + '", login = "' + reg['login'] + '" where idusuarios = ' + str(reg['idusuario'])
        retorno = self.execute(banco, query)

        # query = 'update {0}.{1} set nome = "{2}", ativo = "{4}", login="{5}" where idusuarios = {3}'.format(banco, tb_usuarios, 
        #     reg['nome'],
        #     reg['idusuario'],
        #     reg['ativo'],
        #     reg['login']
        #     ) 

