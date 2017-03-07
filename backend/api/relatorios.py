# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

import MySQLdb
from sqlalchemy import create_engine

def relatorio():
    # Establish a MySQL Connection
    # ipservidor = "127.0.0.1" # LOCAL
    ipservidor = "200.98.174.103" # UOLHOST

    usuario    = "root"
    senha      = "lelo$321"
    banco      = "dbContabil"

    connection = MySQLdb.connect (host=ipservidor, user=usuario, passwd=senha, db=banco)

    query = '''
        SELECT a.codigo, a.descricao,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2015
                and b.mes = 01
                and b.idplano = a.codigo
            ) Janeiro2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2016
                and b.mes = 01
                and b.idplano = a.codigo
            ) Janeiro2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2015
                and b.mes = 02
                and b.idplano = a.codigo
            ) Fevereiro2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2016
                and b.mes = 02
                and b.idplano = a.codigo
            ) Fevereiro2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2015
                and b.mes = 03
                and b.idplano = a.codigo
            ) Marco2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2016
                and b.mes = 03
                and b.idplano = a.codigo
            ) Marco2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2015
                and b.mes = 04
                and b.idplano = a.codigo
            ) Abril2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2016
                and b.mes = 04
                and b.idplano = a.codigo
            ) Abril2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2015
                and b.mes = 05
                and b.idplano = a.codigo
            ) Maio2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2016
                and b.mes = 05
                and b.idplano = a.codigo
            ) Maio2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2015
                and b.mes = 06
                and b.idplano = a.codigo
            ) Junho2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2016
                and b.mes = 06
                and b.idplano = a.codigo
            ) Junho2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2015
                and b.mes = 07
                and b.idplano = a.codigo
            ) Julho2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2016
                and b.mes = 07
                and b.idplano = a.codigo
            ) Julho2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2015
                and b.mes = 08
                and b.idplano = a.codigo
            ) Agosto2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2016
                and b.mes = 08
                and b.idplano = a.codigo
            ) Agosto2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2015
                and b.mes = 09
                and b.idplano = a.codigo
            ) Setembro2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2016
                and b.mes = 09
                and b.idplano = a.codigo
            ) Setembro2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2015
                and b.mes = 10
                and b.idplano = a.codigo
            ) Outubro2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2016
                and b.mes = 10
                and b.idplano = a.codigo
            ) Outubro2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2015
                and b.mes = 11
                and b.idplano = a.codigo
            ) Novembro2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2016
                and b.mes = 11
                and b.idplano = a.codigo
            ) Novembro2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2015
                and b.mes = 12
                and b.idplano = a.codigo
            ) Dezembro2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = 2016
                and b.mes = 12
                and b.idplano = a.codigo
            ) Dezembro2016

        FROM dbContabil.cadplano a
        order by a.tipocd desc
    '''

    # result = connection.execute(query)
    cursor = connection.cursor()
    cursor.execute(query)

    for row in cursor:
        print '|' + row[0] + '|' + row[1] + '|' + str(row[2]) + '|'

    cursor.close()
    connection.close()

    # return codigo

class peOficial(tornado.web.RequestHandler):
    def get(self):
        relatorio()
        self.write('teste')

application = tornado.web.Application([
   (r"/peOficial", peOficial)
])

if __name__ == "__main__":
   print('API Rodando na porta 8000...')
   application.listen(8000)
   tornado.ioloop.IOLoop.instance().start()
