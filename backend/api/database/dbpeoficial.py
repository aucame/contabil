# -*- coding: utf-8 -*-

import MySQLdb
from sqlalchemy import create_engine

def limpaarquivo():
    file = open('pdf.html','w')
    file.close()

def gravalinha(linha):
    file = open('pdf.html','a')
    file.write(linha+'\n')
    file.close()

def buscaDados():
    # Establish a MySQL Connection
    # ipservidor = "127.0.0.1" # LOCAL
    ipservidor = "200.98.174.103" # UOLHOST

    usuario    = "root"
    senha      = "lelo$321"
    # senha      = "123456"
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
        order by a.tipocd desc, a.idplano asc
    '''

    # result = connection.execute(query)
    cursor = connection.cursor()
    cursor.execute(query)

    cursor.close()
    connection.close()

    return  cursor

def relatorio():
    limpaarquivo()

    gravalinha('<!DOCTYPE html>')
    gravalinha('<html>')
    gravalinha('<head>')
    gravalinha('<meta charset="UTF-8">')
    gravalinha('<title>D.R.E </title>')

    linha   =   '''
                <style>
                table, th, td {
                    border: 1px solid black;
                    padding: 1px;
                    text-align: right;
                }
                table {
                    border-spacing: 1px;
                }
                body {
                width: 2500px;
                margin: 0 auto;
                }
                </style>
                '''
    gravalinha(linha)

    gravalinha('</head>')
    gravalinha('<body>')

    gravalinha('<table>')

    linha = '<tr>'+ \
            '<th></th>'+ \
            '<th width = "400px">D.R.E. 2.016 X 2.015</th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '<th></th>'+ \
            '</tr>'
    gravalinha(linha)

    linha = '<tr>'+ \
            '<td></td>'+ \
            '<td>D.R.E. ECONÔMICO / FINANCEIRO</td>'+ \
            '<td>2015</td>'+ \
            '<td>2016</td>'+ \
            '<td>2015</td>'+ \
            '<td>2016</td>'+ \
            '<td>2015</td>'+ \
            '<td>2016</td>'+ \
            '<td>2015</td>'+ \
            '<td>2016</td>'+ \
            '<td>2015</td>'+ \
            '<td>2016</td>'+ \
            '<td>2015</td>'+ \
            '<td>2016</td>'+ \
            '<td>2015</td>'+ \
            '<td>2016</td>'+ \
            '<td>2015</td>'+ \
            '<td>2016</td>'+ \
            '<td>2015</td>'+ \
            '<td>2016</td>'+ \
            '<td>2015</td>'+ \
            '<td>2016</td>'+ \
            '<td>2015</td>'+ \
            '<td>2016</td>'+ \
            '<td>2015</td>'+ \
            '<td>2016</td>'+ \
            '</tr>'
    gravalinha(linha)

    linha = '<tr>'+ \
            '<td></td>'+ \
            '<td>EXERCICIOS : 2.016 X 2.015</td>'+ \
            '<td>Janeiro</td>'+ \
            '<td>Janeiro</td>'+ \
            '<td>Fevereiro</td>'+ \
            '<td>Fevereiro</td>'+ \
            '<td>Marco</td>'+ \
            '<td>Marco</td>'+ \
            '<td>Abril</td>'+ \
            '<td>Abril</td>'+ \
            '<td>Maio</td>'+ \
            '<td>Maio</td>'+ \
            '<td>Junho</td>'+ \
            '<td>Junho</td>'+ \
            '<td>Julho</td>'+ \
            '<td>Julho</td>'+ \
            '<td>Agosto</td>'+ \
            '<td>Agosto</td>'+ \
            '<td>Setembro</td>'+ \
            '<td>Setembro</td>'+ \
            '<td>Outubro</td>'+ \
            '<td>Outubro</td>'+ \
            '<td>Novembro</td>'+ \
            '<td>Novembro</td>'+ \
            '<td>Dezembro</td>'+ \
            '<td>Dezembro</td>'+ \
            '</tr>'
    gravalinha(linha)

    linha = '<tr>'+ \
            '<td>CONTABIL</td>'+ \
            '<td>JANEIRO A DEZEMBRO</td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '<td></td>'+ \
            '</tr>'
    gravalinha(linha)

    dados = buscaDados()
    for row in dados:
        linha = '<tr>' + \
                '<td>' + str(row[0])+'</td>' + \
                '<td align="left">' + str(row[1])+'</td>' + \
                '<td>' + str(row[2])+'</td>' + \
                '<td>' + str(row[3])+'</td>' + \
                '<td>' + str(row[4])+'</td>' + \
                '<td>' + str(row[5])+'</td>' + \
                '<td>' + str(row[6])+'</td>' + \
                '<td>' + str(row[7])+'</td>' + \
                '<td>' + str(row[8])+'</td>' + \
                '<td>' + str(row[9])+'</td>' + \
                '<td>' + str(row[10])+'</td>' + \
                '<td>' + str(row[11])+'</td>' + \
                '<td>' + str(row[12])+'</td>' + \
                '<td>' + str(row[13])+'</td>' + \
                '<td>' + str(row[14])+'</td>' + \
                '<td>' + str(row[15])+'</td>' + \
                '<td>' + str(row[16])+'</td>' + \
                '<td>' + str(row[17])+'</td>' + \
                '<td>' + str(row[18])+'</td>' + \
                '<td>' + str(row[19])+'</td>' + \
                '<td>' + str(row[20])+'</td>' + \
                '<td>' + str(row[21])+'</td>' + \
                '<td>' + str(row[22])+'</td>' + \
                '<td>' + str(row[23])+'</td>' + \
                '<td>' + str(row[24])+'</td>' + \
                '<td>' + str(row[25])+'</td>' + \
                '</tr>'
        gravalinha(linha)

    gravalinha('</table>')
    gravalinha('</body>')
    gravalinha('</html>')
