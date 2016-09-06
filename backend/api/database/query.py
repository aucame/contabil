import json
import codecs
import pymysql
from configuration import database
from datetime import date, timedelta
from sqlalchemy import create_engine

class OracleQuery():
    def execute(self,db,query):
        database_settings = database.Settings()

        # Set database to query
        database_settings.setDatabase(db)

        str_conn = '''oracle+cx_oracle://{0}:{1}@{2}:{3}/{4}
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

class MySqlQuery():
    def execute(self,db,query):
        database_settings = database.Settings()
        # Set database to query
        database_settings.setDatabase(db)

        try:
           connection = pymysql.connect(
               user = database_settings.user(),
               password = database_settings.password(),
               host = database_settings.host(),
               database = database_settings.database(),
               port = database_settings.port()
           )

           cursor = connection.cursor()

           cursor.execute(query)

           return cursor.fetchall()

        finally:
            cursor.close()
            connection.close()

    def product_by_average_ticket(self,api_type,line,families,number_of_days):
        product_list = []
        join_query = [];
        date_now = date.today()
        date_subtracted = date_now - timedelta(days=number_of_days)

        # Security issue
        if api_type == 'subcategory':
          column = 'Subcategory'
        elif api_type == 'productgroup':
          column = 'Group'
        elif api_type == 'specifications':
          column = 'Specifications'
        elif api_type == 'brand':
          column = 'Brand'
        else:
          column = 'Subcategory'

        query = '''
              select
                p.IBMCode productid,
                if(sum(s.ItemValue) / sum(s.ItemQuantity) > 0, sum(s.ItemValue) / sum(s.ItemQuantity), p.Price) average_transaction_value
              FROM
                ProductDimension p
              LEFT JOIN
                Sales s ON s.Product = p.IBMCode
              WHERE
                p.Category = {0}
              AND
                s.OriginDate >= '{1}'
              AND
                ('''.format(int(line),
                              date_subtracted)

        # mount the query for each item in families parameter
        for item in families:
          join_query.append(
            '''
                p.{0} = {1}
            '''.format(column,
                      int(item)))

        # concatenate the query
        query = query + ' OR '.join(join_query) + ' )'

        if api_type == 'specifications':
          query = query + ' AND p.Subcategory = 2 group by s.Product'
        else:
          query = query + ' group by s.Product'

        data = self.execute('boto', query)

        for value in data:
            product_list.append({'id': value[0], 'average_ticket': float(value[1])})

        products = {'products': product_list}

        return products

    def get_sortimento(self, product_data):
      initial_product_list = product_data
      sortimento_list, temp_list, query_list = [], [], []

      # if get products
      if(len(product_data['products']) > 0):

        query = '''
            SELECT DISTINCT
                (p.IBMCode) AS productid
            FROM
              ProductDimension p
                    INNER JOIN
                Sortimento s ON p.IBMCode = s.ProductId
            WHERE ('''

        subquery = ""

        for item in product_data['products']:
          item_id = int(item['id'])
          subquery += 'p.IBMCode = ' + str(item_id) + ' OR '

        query += subquery[:-3]

        query += ''') AND
            (s.HasSortimento = 1 or s.HasPortal = 1)
          '''.format(query_list)
        data = self.execute('boto', query)

        for value in data:
          sortimento_list.append(value[0])

        return sortimento_list
      else:
        return False

    def get_block_status(self,category_id, subcategory_id, branch_id=False):
      	sofrimento = []
    	sql = """
                  SELECT b.BranchId as Branch, bs.Name as Status
                  FROM Block b
                  INNER JOIN BlockStatus bs
                  ON b.BlockStatusId = bs.BlockStatusId
                  WHERE
                  b.CodLinha = %s AND b.CodFamilia = %s"""

    	sql = sql % (category_id, subcategory_id)

     	if branch_id:
            sql += " AND b.BranchId = %s"
            sql = sql % (branch_id,)

        data = self.execute('boto', sql)

        data_to_return = dict((x,y) for x, y in data)

        data_to_return = json.dumps(data_to_return, sort_keys = False, indent = 4)

    	return data_to_return
