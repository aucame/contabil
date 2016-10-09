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
            result.append({'idusuarios': value[0], 'nome': value[1]})
    
        retorno = {'cadusuarios': result}
        return retorno

    def cria_usuario(self, data):
        reg = json.loads(data)
        query = 'insert into {0}.{1}(idusuarios, nome, senha, ativo) values ({2}, "{3}", "{4}", {5})'.format(banco, tb_usuarios, 
            reg['idusuarios'], 
            reg['nome'], 
            reg['senha'], 
            int(reg['ativo'])
            )

        retorno = self.execute(banco, query)

    def deleta_usuario(self, data):
        query = 'delete from {0}.{1} where idusuarios = {2}'.format(banco, tb_usuarios, 
            int(data['idusuarios'])
            )
        retorno = self.execute(banco, query)

    def altera_usuario(self, data):
        print(data)
        reg = json.loads(data)
        query = 'update table {0}.{1} set nome = "{2}", ativo = {3} where idusuarios = {4}'.format(banco, tb_usuarios, 
            reg['nome'],
            int(reg['ativo']), 
            reg['idusuarios']
            ) 

#    def getLimitesSku(self, codFamilia, codFilial=False):
#        query = '''
#              SELECT COD_FILIAL, COD_FAMILIA, SUM(NUM_RESTRICAO) QTD_LIMITES
#                FROM USR_GRPLOJAS.MAG_T_GL_LIMITE_SKU
#                WHERE cod_familia = {0}'''.format(int(codFamilia))
#
#     	if codFilial:
#            query += ''' AND COD_FILIAL = {0} '''.format(codFilial)
#
#        query += '''GROUP BY COD_FILIAL, COD_FAMILIA'''
#
#        data = self.execute('mlpsi2', query)
#
#        result = []
#        for value in data:
#            result.append({'Filial': value[0], 'Familia': value[1], 'Limite': value[2] })
#
#        skulimits = {'skulimits': result}
#
#        skulimits = json.dumps(skulimits, sort_keys = False, indent = 4)
#
#        return skulimits
