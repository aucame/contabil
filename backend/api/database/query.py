import json
import codecs
from configuration import database
from datetime import date, timedelta
from sqlalchemy import create_engine

class MySqlQuery():
    def execute(self,db,query):
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
            engine = create_engine(str_conn)
            connection = engine.connect()

            result = connection.execute(query)

            return result

        finally:
            connection.close()

    def get_usuarios(self):
        query = 'select * from new_table'

        data = self.execute('new_schema', query)

        result = []
        for value in data:
            result.append({'codigo': value[0]})
    
        retorno = {'usuarios': result}

        #retorno = json.dumps(retorno, sort_keys = False, indent = 4)

        return retorno

    def getLimitesSku(self, codFamilia, codFilial=False):
        query = '''
              SELECT COD_FILIAL, COD_FAMILIA, SUM(NUM_RESTRICAO) QTD_LIMITES
                FROM USR_GRPLOJAS.MAG_T_GL_LIMITE_SKU
                WHERE cod_familia = {0}'''.format(int(codFamilia))

     	if codFilial:
            query += ''' AND COD_FILIAL = {0} '''.format(codFilial)

        query += '''GROUP BY COD_FILIAL, COD_FAMILIA'''

        data = self.execute('mlpsi2', query)

        result = []
        for value in data:
            result.append({'Filial': value[0], 'Familia': value[1], 'Limite': value[2] })

        skulimits = {'skulimits': result}

        skulimits = json.dumps(skulimits, sort_keys = False, indent = 4)

        return skulimits
