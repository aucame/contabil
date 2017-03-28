# -*- coding: utf-8 -*-

import MySQLdb
from sqlalchemy import create_engine

ipservidor = "127.0.0.1" # LOCAL
# ipservidor = "200.98.174.103" # UOLHOST

usuario    = "root"
# senha      = "lelo$321"
senha      = "123456"
banco      = "dbContabil"

def limpaarquivo():
    file = open('pdf.html','w')
    file.close()

def gravalinha(linha):
    file = open('pdf.html','a')
    file.write(linha+'\n')
    file.close()

def buscaDados(anoini, anofin):
    # Establish a MySQL Connection

    connection = MySQLdb.connect (host=ipservidor, user=usuario, passwd=senha, db=banco)

    query = '''
        SELECT a.codigo, a.descricao,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {0}
                and b.mes = 01
                and b.idplano = a.codigo
            ) Janeiro{0},
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {1}
                and b.mes = 01
                and b.idplano = a.codigo
            ) Janeiro{1},
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {0}
                and b.mes = 02
                and b.idplano = a.codigo
            ) Fevereiro2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {1}
                and b.mes = 02
                and b.idplano = a.codigo
            ) Fevereiro2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {0}
                and b.mes = 03
                and b.idplano = a.codigo
            ) Marco2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {1}
                and b.mes = 03
                and b.idplano = a.codigo
            ) Marco2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {0}
                and b.mes = 04
                and b.idplano = a.codigo
            ) Abril2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {1}
                and b.mes = 04
                and b.idplano = a.codigo
            ) Abril2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {0}
                and b.mes = 05
                and b.idplano = a.codigo
            ) Maio2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {1}
                and b.mes = 05
                and b.idplano = a.codigo
            ) Maio2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {0}
                and b.mes = 06
                and b.idplano = a.codigo
            ) Junho2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {1}
                and b.mes = 06
                and b.idplano = a.codigo
            ) Junho2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {0}
                and b.mes = 07
                and b.idplano = a.codigo
            ) Julho2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {1}
                and b.mes = 07
                and b.idplano = a.codigo
            ) Julho2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {0}
                and b.mes = 08
                and b.idplano = a.codigo
            ) Agosto2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {1}
                and b.mes = 08
                and b.idplano = a.codigo
            ) Agosto2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {0}
                and b.mes = 09
                and b.idplano = a.codigo
            ) Setembro2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {1}
                and b.mes = 09
                and b.idplano = a.codigo
            ) Setembro2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {0}
                and b.mes = 10
                and b.idplano = a.codigo
            ) Outubro2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {1}
                and b.mes = 10
                and b.idplano = a.codigo
            ) Outubro2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {0}
                and b.mes = 11
                and b.idplano = a.codigo
            ) Novembro2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {1}
                and b.mes = 11
                and b.idplano = a.codigo
            ) Novembro2016,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {0}
                and b.mes = 12
                and b.idplano = a.codigo
            ) Dezembro2015,
            (select b.valor 
                from dbContabil.cadlancamento b
                where b.ano = {1}
                and b.mes = 12
                and b.idplano = a.codigo
            ) Dezembro2016

        FROM dbContabil.cadplano a
        order by a.tipocd asc #desc, a.idplano asc
    '''

    query = query.format(anoini, anofin)

    print query

    # result = connection.execute(query)
    cursor = connection.cursor()
    cursor.execute(query)

    cursor.close()
    connection.close()

    return  cursor

def diasuteisTrabalhados(anoini, anofin):
    connection = MySQLdb.connect (host=ipservidor, user=usuario, passwd=senha, db=banco)

    query = '''
        select 'a', 
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {0}
            and b.mes = 01
            and b.idempresa = 1
            ) Janeiro{0},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {1}
            and b.mes = 01
            and b.idempresa = 1
            ) Janeiro{1},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {0}
            and b.mes = 02
            and b.idempresa = 1
            ) Fevereiro{0},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {1}
            and b.mes = 02
            and b.idempresa = 1
            ) Fevereiro{1},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {0}
            and b.mes = 03
            and b.idempresa = 1
            ) Marco{0},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {1}
            and b.mes = 03
            and b.idempresa = 1
            ) Marco{1},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {0}
            and b.mes = 04
            and b.idempresa = 1
            ) Abril{0},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {1}
            and b.mes = 04
            and b.idempresa = 1
            ) Abril{1},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {0}
            and b.mes = 05
            and b.idempresa = 1
            ) Maio{0},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {1}
            and b.mes = 05
            and b.idempresa = 1
            ) Maio{1},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {0}
            and b.mes = 06
            and b.idempresa = 1
            ) Junho{0},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {1}
            and b.mes = 06
            and b.idempresa = 1
            ) Junho{1},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {0}
            and b.mes = 07
            and b.idempresa = 1
            ) Julho{0},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {1}
            and b.mes = 07
            and b.idempresa = 1
            ) Julho{1},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {0}
            and b.mes = 08
            and b.idempresa = 1
            ) Agosto{0},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {1}
            and b.mes = 08
            and b.idempresa = 1
            ) Agosto{1},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {0}
            and b.mes = 09
            and b.idempresa = 1
            ) Setembro{0},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {1}
            and b.mes = 09
            and b.idempresa = 1
            ) Setembro{1},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {0}
            and b.mes = 10
            and b.idempresa = 1
            ) Outubro{0},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {1}
            and b.mes = 10
            and b.idempresa = 1
            ) Outubro{1},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {0}
            and b.mes = 11
            and b.idempresa = 1
            ) Novembro{0},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {1}
            and b.mes = 11
            and b.idempresa = 1
            ) Novembro{1},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {0}
            and b.mes = 12
            and b.idempresa = 1
            ) Dezembro{0},
            (
            select b.diasuteis
            from dbContabil.cadparam b
            where b.ano = {1}
            and b.mes = 12
            and b.idempresa = 1
            ) Dezembro{1}

        from dual
    '''

    query = query.format(anoini, anofin)

    cursor = connection.cursor()
    cursor.execute(query)

    cursor.close()
    connection.close()

    return  cursor

def linhabranca():
    linha = '<tr>'+ \
            '<th>.</th>'     +   \
            '<th></th>'     +   \
            '<th></th>'     +   \
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

def cabecalho(anoini, anofin):
    linha = '<tr>'+ \
            '<th></th>'     +   \
            '<th width = "400px">D.R.E. {0} X {1}</th>'.format(anoini, anofin) + \
            '<th></th>'     +   \
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
            '<td>D.R.E. ECONÔMICO / FINANCEIRO</td>'    + \
            '<td>{0}</td>'.format(anoini) + \
            '<td>{0}</td>'.format(anofin) + \
            '<td>{0}</td>'.format(anoini) + \
            '<td>{0}</td>'.format(anofin) + \
            '<td>{0}</td>'.format(anoini) + \
            '<td>{0}</td>'.format(anofin) + \
            '<td>{0}</td>'.format(anoini) + \
            '<td>{0}</td>'.format(anofin) + \
            '<td>{0}</td>'.format(anoini) + \
            '<td>{0}</td>'.format(anofin) + \
            '<td>{0}</td>'.format(anoini) + \
            '<td>{0}</td>'.format(anofin) + \
            '<td>{0}</td>'.format(anoini) + \
            '<td>{0}</td>'.format(anofin) + \
            '<td>{0}</td>'.format(anoini) + \
            '<td>{0}</td>'.format(anofin) + \
            '<td>{0}</td>'.format(anoini) + \
            '<td>{0}</td>'.format(anofin) + \
            '<td>{0}</td>'.format(anoini) + \
            '<td>{0}</td>'.format(anofin) + \
            '<td>{0}</td>'.format(anoini) + \
            '<td>{0}</td>'.format(anofin) + \
            '<td>{0}</td>'.format(anoini) + \
            '<td>{0}</td>'.format(anofin) + \
            '</tr>'
    gravalinha(linha)

    linha = '<tr>'+ \
            '<td></td>'+ \
            '<td>EXERCICIOS : {0} X {1}</td>'.format(anoini, anofin) + \
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

def relatorio(anoini, anofin):
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

    cabecalho(anoini, anofin)

    linhabranca()

    dados = buscaDados(anoini, anofin)
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

relatorio(2016,2015)
