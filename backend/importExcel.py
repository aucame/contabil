# coding=utf-8


import xlrd
import MySQLdb
from sqlalchemy import create_engine

def verificasetem(codigo, ipservidor, usuario, senha, banco):
    engine = create_engine('mysql://' + usuario + ':' + senha + '@' + ipservidor + '/' + banco)
    # engine = create_engine('mysql://root:123456@200.98.174.103/dbContabil')
    connection = engine.connect()

    flag = 'S'
    while   (flag == 'S'):

        codigo = montaCodigo(codigo)
        query = 'select * from dbContabil.cadplano where codigo = "' + codigo + '"'
        # print(query)
        result = connection.execute(query)

        print query

        numero = int(codigo[13:18])

        if  result.rowcount > 0:
            print 'sim'
            numero += 1
            codigo = codigo[0:13] + str(numero).zfill(5)
            print '...... ' + codigo
        else:
            print 'naooooo'
            flag = 'N'

    connection.close()

    return codigo

def montaCodigo(registro):

    tipo, grupo, subgrupo, subgrp, numero = registro.split('.')

    novo =  tipo.zfill(2) + '.' + \
            grupo.zfill(2) + '.' + \
            subgrupo.zfill(2) + '.' + \
            subgrp.zfill(3) + '.' + \
            numero.zfill(5)

    # print novo

    return novo

def gravaPlano(contplano, registro, descri, tipocd):
    
    tipo, grupo, subgrupo, subgrp, numero = registro.split('.')

    registro =  montaCodigo(registro)

    # print registro

    query = 'insert into dbContabil.cadplano (idplano, codigo, descricao, tipocd, tipo, grupo, subgrupo, subgrp, numero) values (' + \
        str(contplano) + ',"' + registro + '","' + \
        descri + '","' + tipocd + '","' + tipo + '","' + \
        grupo + '","' + subgrupo + '","' + subgrp + '","' + numero + \
        '")'

    cursor.execute(query)

def gravaLancamento(idlancamento, ano, mes, idplano, valor, idcliente):

    idplano = montaCodigo(idplano)

    query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento",
        idlancamento, ano, mes, idplano, valor, idcliente )
    cursor.execute(query)

def gravaParametro(idparam, mes, ano, idempresa, diasuteis, meddiafat, paramostra):
    query = 'insert into {0}.{1} (idparam, mes, ano, idempresa, diasuteis, meddiafat) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadparam", 
        idparam, mes, ano, idempresa, diasuteis, meddiafat, paramostra )
    cursor.execute(query)

def regravaParametro(idparam, mes, ano, idempresa, diasuteis, meddiafat, paramostra):
    if  paramostra > 0:
        query   =   'update dbContabil.cadparam set paramostra = ' + str(paramostra) + ' where mes = ' + str(mes) + ' and ano = ' + str(ano) + ' and idempresa = ' + str(idempresa)
        cursor.execute(query)

# Open the workbook and define the worksheet
book = xlrd.open_workbook("DRE2016X2015.xls")

sheet = book.sheet_by_name("DRE 2.016 X 2.015")
#sheet = book.sheet_by_index(0)

# Establish a MySQL Connection
ipservidor = "127.0.0.1" # LOCAL
# ipservidor = "200.98.174.103" # UOLHOST

usuario    = "root"
senha      = "123456" # LOCAL
# senha      = "lelo$321" # UOLHOST
banco      = "dbContabil"

database = MySQLdb.connect (host=ipservidor, user=usuario, passwd=senha, db=banco)

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

query = 'truncate table dbContabil.cadplano'
cursor.execute(query)

query = 'truncate table dbContabil.cadlancamento' 
cursor.execute(query)

query = 'truncate table dbContabil.cadparam' 
cursor.execute(query)

idchave = 0
contador = 0
contplano = 0
contlancto = 0
contalinha = 0
contlancto2 = 0
contparam = 0

flag = 'S'
valor  = 0.0
valor2 = 0.0
valor3 = 0.0
valor4 = 0.0
valor5 = 0.0
valor6 = 0.0

valor041 = 0.0
valor042 = 0.0
valor051 = 0.0
valor052 = 0.0
valor061 = 0.0
valor062 = 0.0
valor071 = 0.0
valor072 = 0.0
valor081 = 0.0
valor082 = 0.0
valor091 = 0.0
valor092 = 0.0
valor101 = 0.0
valor102 = 0.0
valor111 = 0.0
valor112 = 0.0
valor121 = 0.0
valor122 = 0.0

# Create a for loop to iterate through each row in the xls file, starting from row 2
for r in range(1, sheet.nrows):

    flag = 'S'
    contalinha = contalinha + 1

    codigo = sheet.cell(r,0).value
    descri = sheet.cell(r,1).value

    valor  = sheet.cell(r,3).value
    valor2 = sheet.cell(r,4).value
    valor3 = sheet.cell(r,5).value
    valor4 = sheet.cell(r,6).value
    valor5 = sheet.cell(r,7).value
    valor6 = sheet.cell(r,8).value

    valor041 = sheet.cell(r,9).value
    valor042 = sheet.cell(r,10).value

    valor051 = sheet.cell(r,11).value
    valor052 = sheet.cell(r,12).value

    valor061 = sheet.cell(r,13).value
    valor062 = sheet.cell(r,14).value

    valor071 = sheet.cell(r,15).value
    valor072 = sheet.cell(r,16).value

    valor081 = sheet.cell(r,17).value
    valor082 = sheet.cell(r,18).value

    valor091 = sheet.cell(r,19).value
    valor092 = sheet.cell(r,20).value

    valor101 = sheet.cell(r,21).value
    valor102 = sheet.cell(r,22).value

    valor111 = sheet.cell(r,23).value
    valor112 = sheet.cell(r,24).value

    valor121 = sheet.cell(r,25).value
    valor122 = sheet.cell(r,26).value


    registro = codigo[0:12]

    if  descri == '':
        flag = 'N'

    if  registro == '':
        flag = 'N'

    if  valor == '':
        valor = '0.00'
        valor = float(valor)
    if  valor2 == '':
        valor2 = '0.00'
        valor2 = float(valor2)

    if  valor3 == '':
        valor3 = '0.00'
        valor3 = float(valor3)
    if  valor4 == '':
        valor4 = '0.00'
        valor4 = float(valor4)

    if  valor5 == '':
        valor5 = '0.00'
        valor5 = float(valor5)

    if  valor6 == '':
        valor6 = '0.00'
        valor6 = float(valor6)

    if  valor041 == '':
        valor041 = '0.00'
        valor041 = float(valor041)
    if  valor042 == '':
        valor042 = '0.00'
        valor042 = float(valor042)

    if  valor051 == '':
        valor051 = '0.00'
        valor051 = float(valor051)
    if  valor052 == '':
        valor052 = '0.00'
        valor052 = float(valor052)

    if  valor061 == '':
        valor061 = '0.00'
        valor061 = float(valor061)
    if  valor062 == '':
        valor062 = '0.00'
        valor062 = float(valor062)

    if  valor071 == '':
        valor071 = '0.00'
        valor071 = float(valor071)
    if  valor072 == '':
        valor072 = '0.00'
        valor072 = float(valor072)

    if  valor081 == '':
        valor081 = '0.00'
        valor081 = float(valor081)
    if  valor082 == '':
        valor082 = '0.00'
        valor082 = float(valor082)

    if  valor091 == '':
        valor091 = '0.00'
        valor091 = float(valor091)
    if  valor092 == '':
        valor092 = '0.00'
        valor092 = float(valor092)

    if  valor101 == '':
        valor101 = '0.00'
        valor101 = float(valor101)
    if  valor102 == '':
        valor102 = '0.00'
        valor102 = float(valor102)

    if  valor111 == '':
        valor111 = '0.00'
        valor111 = float(valor111)
    if  valor112 == '':
        valor112 = '0.00'
        valor112 = float(valor112)

    if  valor121 == '':
        valor121 = '0.00'
        valor121 = float(valor121)
    if  valor122 == '':
        valor122 = '0.00'
        valor122 = float(valor122)

    if  contalinha == 9:

        contparam = contparam + 1
        gravaParametro(contparam, 1, 2016, 1, round(valor,0), 0, 0)
        contparam = contparam + 1
        gravaParametro(contparam, 1, 2015, 1, round(valor2,0), 0, 0)

        contparam = contparam + 1
        gravaParametro(contparam, 2, 2016, 1, round(valor3,0), 0, 0)
        contparam = contparam + 1
        gravaParametro(contparam, 2, 2015, 1, round(valor4,0), 0, 0)

        contparam = contparam + 1
        gravaParametro(contparam, 3, 2016, 1, round(valor5,0), 0, 0)
        contparam = contparam + 1
        gravaParametro(contparam, 3, 2015, 1, round(valor6,0), 0, 0)

        contparam = contparam + 1
        gravaParametro(contparam, 4, 2016, 1, round(valor041,0), 0, 0)
        contparam = contparam + 1
        gravaParametro(contparam, 4, 2015, 1, round(valor042,0), 0, 0)

        contparam = contparam + 1
        gravaParametro(contparam, 5, 2016, 1, round(valor051,0), 0, 0)
        contparam = contparam + 1
        gravaParametro(contparam, 5, 2015, 1, round(valor052,0), 0, 0)

        contparam = contparam + 1
        gravaParametro(contparam, 6, 2016, 1, round(valor061,0), 0, 0)
        contparam = contparam + 1
        gravaParametro(contparam, 6, 2015, 1, round(valor062,0), 0, 0)

        contparam = contparam + 1
        gravaParametro(contparam, 7, 2016, 1, round(valor071,0), 0, 0)
        contparam = contparam + 1
        gravaParametro(contparam, 7, 2015, 1, round(valor072,0), 0, 0)

        contparam = contparam + 1
        gravaParametro(contparam, 8, 2016, 1, round(valor081,0), 0, 0)
        contparam = contparam + 1
        gravaParametro(contparam, 8, 2015, 1, round(valor082,0), 0, 0)

        contparam = contparam + 1
        gravaParametro(contparam, 9, 2016, 1, round(valor091,0), 0, 0)
        contparam = contparam + 1
        gravaParametro(contparam, 9, 2015, 1, round(valor092,0), 0, 0)

        contparam = contparam + 1
        gravaParametro(contparam, 10, 2016, 1, round(valor101,0), 0, 0)
        contparam = contparam + 1
        gravaParametro(contparam, 10, 2015, 1, round(valor102,0), 0, 0)

        contparam = contparam + 1
        gravaParametro(contparam, 11, 2016, 1, round(valor111,0), 0, 0)
        contparam = contparam + 1
        gravaParametro(contparam, 11, 2015, 1, round(valor112,0), 0, 0)

        contparam = contparam + 1
        gravaParametro(contparam, 12, 2016, 1, round(valor121,0), 0, 0)
        contparam = contparam + 1
        gravaParametro(contparam, 12, 2015, 1, round(valor122,0), 0, 0)


    if  contalinha == 26:
        regravaParametro(0, 1, 2016, 1, 0, 0, round(valor,0))
        regravaParametro(0, 1, 2015, 1, 0, 0, round(valor2,0))
        regravaParametro(0, 2, 2016, 1, 0, 0, round(valor3,0))
        regravaParametro(0, 2, 2015, 1, 0, 0, round(valor4,0))
        regravaParametro(0, 3, 2016, 1, 0, 0, round(valor5,0))
        regravaParametro(0, 3, 2015, 1, 0, 0, round(valor6,0))
        regravaParametro(0, 4, 2016, 1, 0, 0, round(valor041,0))
        regravaParametro(0, 4, 2015, 1, 0, 0, round(valor042,0))
        regravaParametro(0, 5, 2016, 1, 0, 0, round(valor051,0))
        regravaParametro(0, 5, 2015, 1, 0, 0, round(valor052,0))
        regravaParametro(0, 6, 2016, 1, 0, 0, round(valor061,0))
        regravaParametro(0, 6, 2015, 1, 0, 0, round(valor062,0))
        regravaParametro(0, 7, 2016, 1, 0, 0, round(valor071,0))
        regravaParametro(0, 7, 2015, 1, 0, 0, round(valor072,0))
        regravaParametro(0, 8, 2016, 1, 0, 0, round(valor081,0))
        regravaParametro(0, 8, 2015, 1, 0, 0, round(valor082,0))
        regravaParametro(0, 9, 2016, 1, 0, 0, round(valor091,0))
        regravaParametro(0, 9, 2015, 1, 0, 0, round(valor092,0))
        regravaParametro(0, 10, 2016, 1, 0, 0, round(valor101,0))
        regravaParametro(0, 10, 2015, 1, 0, 0, round(valor102,0))
        regravaParametro(0, 11, 2016, 1, 0, 0, round(valor111,0))
        regravaParametro(0, 11, 2015, 1, 0, 0, round(valor112,0))
        regravaParametro(0, 12, 2016, 1, 0, 0, round(valor121,0))
        regravaParametro(0, 12, 2015, 1, 0, 0, round(valor122,0))


    if  flag == 'S':
        flag = 'N'
        if  contalinha >= 11 and contalinha <= 13:
            flag = 'S'
        if  contalinha >= 21 and contalinha <= 22:
            flag = 'S'
        if  contalinha >= 55 and contalinha <= 71:
            flag = 'S'
        if  contalinha >= 90 and contalinha <= 97:
            flag = 'S'
        if  contalinha >= 118 and contalinha <= 146:
            flag = 'S'
        if  contalinha >= 157 and contalinha <= 171:
            flag = 'S'
        if  contalinha >= 183 and contalinha <= 204:
            flag = 'S'
        if  contalinha >= 215 and contalinha <= 242:
            flag = 'S'
        if  contalinha >= 253 and contalinha <= 316:
            flag = 'S'
        if  contalinha >= 327 and contalinha <= 342:
            flag = 'S'
        if  contalinha >= 353 and contalinha <= 363:
            flag = 'S'
        if  contalinha >= 383 and contalinha <= 385:
            flag = 'S'
        if  contalinha >= 396 and contalinha <= 399:
            flag = 'S'
        if  contalinha >= 410 and contalinha <= 420:
            flag = 'S'
        if  contalinha >= 431 and contalinha <= 456:
            flag = 'S'
        if  contalinha >= 467 and contalinha <= 470:
            flag = 'S'
        if  contalinha >= 489 and contalinha <= 509:
            flag = 'S'
        if  contalinha >= 519 and contalinha <= 531:
            flag = 'S'
        if  contalinha >= 582 and contalinha <= 585:
            flag = 'S'


        # print(str(contalinha) + ' - ' + flag + ' - ' + str(valor) + ' - ' )

    if  flag == 'S':
        try:
            valor = round(valor,2)
        except Exception as e:
            flag = 'N'
        
    if  flag == 'S':
        try:
            valor2 = round(valor2,2)
        except Exception as e:
            flag = 'N'

    if  flag == 'S':
        try:
            valor3 = round(valor3,2)
        except Exception as e:
            flag = 'N'

    if  flag == 'S':
        try:
            valor4 = round(valor4,2)
        except Exception as e:
            flag = 'N'

    if  flag == 'S':
        try:
            valor5 = round(valor5,2)
        except Exception as e:
            flag = 'N'

    if  flag == 'S':
        try:
            valor6 = round(valor6,2)
        except Exception as e:
            flag = 'N'

    if  flag == 'S':
        try:
            valor041 = round(valor041,2)
        except Exception as e:
            flag = 'N'
    if  flag == 'S':
        try:
            valor042 = round(valor042,2)
        except Exception as e:
            flag = 'N'

    if  flag == 'S':
        try:
            valor051 = round(valor051,2)
        except Exception as e:
            flag = 'N'
    if  flag == 'S':
        try:
            valor052 = round(valor052,2)
        except Exception as e:
            flag = 'N'

    if  flag == 'S':
        try:
            valor061 = round(valor061,2)
        except Exception as e:
            flag = 'N'
    if  flag == 'S':
        try:
            valor062 = round(valor062,2)
        except Exception as e:
            flag = 'N'

    if  flag == 'S':
        try:
            valor071 = round(valor071,2)
        except Exception as e:
            flag = 'N'
    if  flag == 'S':
        try:
            valor072 = round(valor072,2)
        except Exception as e:
            flag = 'N'

    if  flag == 'S':
        try:
            valor081 = round(valor081,2)
        except Exception as e:
            flag = 'N'
    if  flag == 'S':
        try:
            valor082 = round(valor082,2)
        except Exception as e:
            flag = 'N'

    if  flag == 'S':
        try:
            valor091 = round(valor091,2)
        except Exception as e:
            flag = 'N'
    if  flag == 'S':
        try:
            valor092 = round(valor092,2)
        except Exception as e:
            flag = 'N'

    if  flag == 'S':
        try:
            valor101 = round(valor101,2)
        except Exception as e:
            flag = 'N'
    if  flag == 'S':
        try:
            valor102 = round(valor102,2)
        except Exception as e:
            flag = 'N'

    if  flag == 'S':
        try:
            valor111 = round(valor111,2)
        except Exception as e:
            flag = 'N'
    if  flag == 'S':
        try:
            valor112 = round(valor112,2)
        except Exception as e:
            flag = 'N'

    if  flag == 'S':
        try:
            valor121 = round(valor121,2)
        except Exception as e:
            flag = 'N'
    if  flag == 'S':
        try:
            valor122 = round(valor122,2)
        except Exception as e:
            flag = 'N'

    if  flag == 'S':
        registro = verificasetem(registro, ipservidor, usuario, senha, banco)

        # print(str(contalinha) + ' --- ' + flag + ' --- ' + str(valor))

    if  flag == 'S':
        contplano = contplano + 1

        tipocd = ''

        if  (codigo[0:1] == '4'):
            tipocd = 'C'

        if  (codigo[0:1] == '3'):
            tipocd = 'D'

        if  (codigo[0:1] == '2'):
            tipocd = 'C'

#       Grava Plano de contas
        gravaPlano(contplano, registro, descri, tipocd)

#       Grava os lançamentos

#       JANEIRO
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2016, 1, registro, valor, 1)
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2015, 1, registro, valor2, 1)

#       FEVEREIRO
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2016, 2, registro, valor3, 1)
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2015, 2, registro, valor4, 1)

#       MARÇO
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2016, 3, registro, valor5, 1)
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2015, 3, registro, valor6, 1)

#       ABRIL
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2016, 4, registro, valor041, 1)
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2015, 4, registro, valor042, 1)

#       MAIO
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2016, 5, registro, valor051, 1)
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2015, 5, registro, valor052, 1)

#       JUNHO
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2016, 6, registro, valor061, 1)
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2015, 6, registro, valor062, 1)

#       JULHO
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2016, 7, registro, valor071, 1)
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2015, 7, registro, valor072, 1)

#       AGOSTO
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2016, 8, registro, valor081, 1)
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2015, 8, registro, valor082, 1)

#       SETEMBRO
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2016, 9, registro, valor091, 1)
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2015, 9, registro, valor092, 1)

#       OUTUBRO
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2016, 10, registro, valor101, 1)
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2015, 10, registro, valor102, 1)

#       NOVEMBRO
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2016, 11, registro, valor111, 1)
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2015, 11, registro, valor112, 1)

#       DEZEMBRO
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2016, 12, registro, valor121, 1)
        contlancto = contlancto + 1
        gravaLancamento(contlancto, 2015, 12, registro, valor122, 1)

#       COMMIT
        database.commit()


# Close the cursor
cursor.close()

#Commit the transaction
database.commit()

#Close the database connection
database.close()

print ''
print 'Planilha importada com sucesso... {0} linhas.'.format(contlancto)
