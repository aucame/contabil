# -*- coding: UTF-8 -*-

import MySQLdb
from sqlalchemy import create_engine


ipservidor  = "127.0.0.1" # LOCAL
# ipservidor = "200.98.174.103" # UOLHOST

usuario     = "root"
# senha      = "lelo$321"
senha       = "123456"
banco       = "dbContabil"

totlinha    =   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def moeda(valor):
    # if valor != None:
    #     import locale
    #     locale.setlocale( locale.LC_ALL, '' )
    #     return locale.currency( valor, grouping=True )
    # return ''
    return valor

def limpaarquivo():
    file = open('pdf.html','w')
    file.close()

def gravalinha(linha):
    file.write(linha+'\n')

def buscaDados(anoini, anofin):
    # Establish a MySQL Connection

    connection = MySQLdb.connect (host=ipservidor, user=usuario, passwd=senha, db=banco, charset="utf8", use_unicode = True)

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
            ) Dezembro2016,
            a.grupoplano

        FROM dbContabil.cadplano a
        order by a.tipocd asc, a.grupoplano asc
    '''

        # order by a.tipocd asc #desc, a.idplano asc

    query = query.format(anoini, anofin)

    # print query

    # result = connection.execute(query)
    cursor = connection.cursor()
    cursor.execute(query)

    cursor.close()
    connection.close()

    return  cursor

def diasuteis(anoini, anofin):
    connection = MySQLdb.connect (host=ipservidor, user=usuario, passwd=senha, db=banco)

    query = '''
        select 'a', 'b',
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
    linha = '<tr>'          +   \
            '<td>.</td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
            '<td></td>'     +   \
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
            '<th></th>'+ \
            '<th></th>'+ \
            '</tr>'
    gravalinha(linha)

    linha = '<tr>'+ \
            '<td></td>'+ \
            '<td>D.R.E. ECONÔMICO / FINANCEIRO</td>' + \
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
            '<td></td>'+ \
            '<td></td>'+ \
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
            '<td>ACUMULADO</td>'+ \
            '<td>ACUMULADO</td>'+ \
            '</tr>'
    gravalinha(linha)

    linha = '<tr>'+ \
            '<td>CONTABIL</td>'+ \
            '<td>JANEIRO A DEZEMBRO</td>'+ \
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
            '<td>{0}</td>'.format(anoini) + \
            '<td>{0}</td>'.format(anofin) + \
            '</tr>'
    gravalinha(linha)

def zeralinha():
    totlinha[2]  = 0
    totlinha[3]  = 0
    totlinha[4]  = 0
    totlinha[5]  = 0
    totlinha[6]  = 0
    totlinha[7]  = 0
    totlinha[8]  = 0
    totlinha[9]  = 0
    totlinha[10] = 0
    totlinha[11] = 0
    totlinha[12] = 0
    totlinha[13] = 0
    totlinha[14] = 0
    totlinha[15] = 0
    totlinha[16] = 0
    totlinha[17] = 0
    totlinha[18] = 0
    totlinha[19] = 0
    totlinha[20] = 0
    totlinha[21] = 0
    totlinha[22] = 0
    totlinha[23] = 0
    totlinha[24] = 0
    totlinha[25] = 0

def somalinha(linha):
    totlinha[2] += linha[2]
    totlinha[3] += linha[3]
    totlinha[4] += linha[4]
    totlinha[5] += linha[5]
    totlinha[6] += linha[6]
    totlinha[7] += linha[7]
    totlinha[8] += linha[8]
    totlinha[9] += linha[9]
    totlinha[10] += linha[10]
    totlinha[11] += linha[11]
    totlinha[12] += linha[12]
    totlinha[13] += linha[13]
    totlinha[14] += linha[14]
    totlinha[15] += linha[15]
    totlinha[16] += linha[16]
    totlinha[17] += linha[17]
    totlinha[18] += linha[18]
    totlinha[19] += linha[19]
    totlinha[20] += linha[20]
    totlinha[21] += linha[21]
    totlinha[22] += linha[22]
    totlinha[23] += linha[23]
    totlinha[24] += linha[24]
    totlinha[25] += linha[25]

def totalgrupo():
    linha = '<tr>' + \
            '<td></td>' + \
            '<td></td>' + \
            '<td>' + str(totlinha[2])+'</td>' + \
            '<td>' + str(totlinha[3])+'</td>' + \
            '<td>' + str(totlinha[4])+'</td>' + \
            '<td>' + str(totlinha[5])+'</td>' + \
            '<td>' + str(totlinha[6])+'</td>' + \
            '<td>' + str(totlinha[7])+'</td>' + \
            '<td>' + str(totlinha[8])+'</td>' + \
            '<td>' + str(totlinha[9])+'</td>' + \
            '<td>' + str(totlinha[10])+'</td>' + \
            '<td>' + str(totlinha[11])+'</td>' + \
            '<td>' + str(totlinha[12])+'</td>' + \
            '<td>' + str(totlinha[13])+'</td>' + \
            '<td>' + str(totlinha[14])+'</td>' + \
            '<td>' + str(totlinha[15])+'</td>' + \
            '<td>' + str(totlinha[16])+'</td>' + \
            '<td>' + str(totlinha[17])+'</td>' + \
            '<td>' + str(totlinha[18])+'</td>' + \
            '<td>' + str(totlinha[19])+'</td>' + \
            '<td>' + str(totlinha[20])+'</td>' + \
            '<td>' + str(totlinha[21])+'</td>' + \
            '<td>' + str(totlinha[22])+'</td>' + \
            '<td>' + str(totlinha[23])+'</td>' + \
            '<td>' + str(totlinha[24])+'</td>' + \
            '<td>' + str(totlinha[25])+'</td>' + \
            '<td></td>' + \
            '<td></td>' + \
            '</tr>'
    gravalinha(linha)

    zeralinha()

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

    wgrupoplano = ''

    # Dias Uteis
    dados = diasuteis(anoini, anofin)
    for row in dados:
        linha = '<tr>' + \
                '<td></td>' + \
                '<td align="left"> Dias Uteis </td>' + \
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
                '<td></td>' + \
                '<td></td>' + \
                '</tr>'
        gravalinha(linha)

    dados = buscaDados(anoini, anofin)
    for row in dados:

        # print row

        somaini =   float(row[2])  + float(row[4])  + float(row[6])  + float(row[8])  + \
                    float(row[10]) + float(row[12]) + float(row[14]) + float(row[16]) + \
                    float(row[18]) + float(row[20]) + float(row[22]) + float(row[24])

        somafin =   float(row[3])  + float(row[5])  + float(row[7])  + float(row[9])  + \
                    float(row[11]) + float(row[13]) + float(row[15]) + float(row[17]) + \
                    float(row[19]) + float(row[21]) + float(row[23]) + float(row[25])

        linha = '<tr>' + \
                '<td>' + str(row[0])+'</td>' + \
                '<td align="left">' + row[1] +'</td>' + \
                '<td>' + str(moeda(row[2]))+'</td>' + \
                '<td>' + str(moeda(row[3]))+'</td>' + \
                '<td>' + str(moeda(row[4]))+'</td>' + \
                '<td>' + str(moeda(row[5]))+'</td>' + \
                '<td>' + str(moeda(row[6]))+'</td>' + \
                '<td>' + str(moeda(row[7]))+'</td>' + \
                '<td>' + str(moeda(row[8]))+'</td>' + \
                '<td>' + str(moeda(row[9]))+'</td>' + \
                '<td>' + str(moeda(row[10]))+'</td>' + \
                '<td>' + str(moeda(row[11]))+'</td>' + \
                '<td>' + str(moeda(row[12]))+'</td>' + \
                '<td>' + str(moeda(row[13]))+'</td>' + \
                '<td>' + str(moeda(row[14]))+'</td>' + \
                '<td>' + str(moeda(row[15]))+'</td>' + \
                '<td>' + str(moeda(row[16]))+'</td>' + \
                '<td>' + str(moeda(row[17]))+'</td>' + \
                '<td>' + str(moeda(row[18]))+'</td>' + \
                '<td>' + str(moeda(row[19]))+'</td>' + \
                '<td>' + str(moeda(row[20]))+'</td>' + \
                '<td>' + str(moeda(row[21]))+'</td>' + \
                '<td>' + str(moeda(row[22]))+'</td>' + \
                '<td>' + str(moeda(row[23]))+'</td>' + \
                '<td>' + str(moeda(row[24]))+'</td>' + \
                '<td>' + str(moeda(row[25]))+'</td>' + \
                '<td>' + str(moeda(somaini))+'</td>' + \
                '<td>' + str(moeda(somafin))+'</td>' + \
                '</tr>'

        if  wgrupoplano ==  '':
            wgrupoplano =   row[26]
            somalinha(row)
        else:
            if  wgrupoplano <> row[26]:
                wgrupoplano =  row[26]
                totalgrupo()
                linhabranca()
                somalinha(row)
            else:
                somalinha(row)
               

        linha = linha.encode('utf-8')
        gravalinha(linha)

    totalgrupo()

    gravalinha('</table>')
    gravalinha('</body>')
    gravalinha('</html>')

file = open('pdf.html','a')
relatorio(2016,2015)
file.close()
