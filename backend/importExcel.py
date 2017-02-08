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
        query = 'select * from dbContabil.cadplano where codigo = "' + codigo + '"'
        # print(query)
        result = connection.execute(query)
        numero = int(codigo[9:12])
        if  result.rowcount > 0:
            numero = numero + 1
            codigo = codigo[0:9] + str(numero).zfill(3)
        else:
            flag = 'N'

    connection.close()

    return codigo

# Open the workbook and define the worksheet
book = xlrd.open_workbook("DRE2016X2015.xls")

sheet = book.sheet_by_name("DRE 2.016 X 2.015")
#sheet = book.sheet_by_index(0)

# Establish a MySQL Connection
# ipservidor = "127.0.0.1" # LOCAL
ipservidor = "200.98.174.103" # UOLHOST

usuario    = "root"
senha      = "123456"
banco      = "dbContabil"

database = MySQLdb.connect (host=ipservidor, user=usuario, passwd=senha, db=banco)

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

query = 'truncate table dbContabil.cadplano'
cursor.execute(query)

query = 'truncate table dbContabil.cadlancamento' 
cursor.execute(query)

idchave = 0
contador = 0
contplano = 0
contlancto = 0
contalinha = 0
contlancto2 = 0

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

        query = 'insert into dbContabil.cadplano (idplano, codigo, descricao, tipocd) values (' + str(contplano) + ',"' + registro + '","' + descri + '","' + tipocd + '")'
        cursor.execute(query)

#       Grava os lançamentos

#       JANEIRO

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2016, 
            01, 
            registro,
            valor,
            1
            )

        print query

        cursor.execute(query)

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2015, 
            01, 
            registro,
            valor2,
            1
            )

        cursor.execute(query)

#       FEVEREIRO

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2016, 
            02, 
            registro,
            valor3,
            1
            )

        print query

        cursor.execute(query)

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2015, 
            02, 
            registro,
            valor4,
            1
            )

        cursor.execute(query)

#       MARÇO

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2016, 
            03, 
            registro,
            valor5,
            1
            )

        print query

        cursor.execute(query)

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2015, 
            03, 
            registro,
            valor6,
            1
            )

        cursor.execute(query)

#       ABRIL

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2016, 
            04, 
            registro,
            valor041,
            1
            )

        print query

        cursor.execute(query)

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2015, 
            04, 
            registro,
            valor042,
            1
            )

        cursor.execute(query)

#       MAIO

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2016, 
            05, 
            registro,
            valor051,
            1
            )

        print query

        cursor.execute(query)

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2015, 
            05, 
            registro,
            valor052,
            1
            )

        cursor.execute(query)

#       JUNHO

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2016, 
            06, 
            registro,
            valor061,
            1
            )

        print query

        cursor.execute(query)

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2015, 
            06, 
            registro,
            valor062,
            1
            )

        cursor.execute(query)

#       JULHO

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2016, 
            07, 
            registro,
            valor071,
            1
            )

        print query

        cursor.execute(query)

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2015, 
            07, 
            registro,
            valor072,
            1
            )

        cursor.execute(query)

#       AGOSTO

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2016, 
            8, 
            registro,
            valor081,
            1
            )

        print query

        cursor.execute(query)

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2015, 
            8, 
            registro,
            valor082,
            1
            )

        cursor.execute(query)

#       SETEMBRO

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2016, 
            9, 
            registro,
            valor091,
            1
            )

        print query

        cursor.execute(query)

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2015, 
            9, 
            registro,
            valor092,
            1
            )

        cursor.execute(query)

#       OUTUBRO

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2016, 
            10, 
            registro,
            valor101,
            1
            )

        print query

        cursor.execute(query)

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2015, 
            10, 
            registro,
            valor102,
            1
            )

        cursor.execute(query)

#       NOVEMBRO

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2016, 
            11, 
            registro,
            valor111,
            1
            )

        print query

        cursor.execute(query)

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2015, 
            11, 
            registro,
            valor112,
            1
            )

        cursor.execute(query)

#       DEZEMBRO

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2016, 
            12, 
            registro,
            valor121,
            1
            )

        print query

        cursor.execute(query)

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2015, 
            12, 
            registro,
            valor122,
            1
            )

        cursor.execute(query)

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
