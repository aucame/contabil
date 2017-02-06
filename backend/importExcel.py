# coding=utf-8

import xlrd
import MySQLdb
from sqlalchemy import create_engine

def verificasetem(codigo):
    query = 'select * from dbContabil.cadplano where codigo = "' + codigo + '"'

    # print query + str(dir(data))

    engine = create_engine('mysql://root:123456@127.0.0.1/dbContabil')
    connection = engine.connect()
    result = connection.execute(query)
    print query + ' - ' + str(result.rowcount)

    # for row in result:
    #     print("codigo: ", row['codigo'])

    connection.close()

# Open the workbook and define the worksheet
book = xlrd.open_workbook("DRE2016X2015.xls")

sheet = book.sheet_by_name("DRE 2.016 X 2.015")
#sheet = book.sheet_by_index(0)

# Establish a MySQL Connection
database = MySQLdb.connect (host="127.0.0.1", user="root", passwd="123456", db="dbContabil")

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
valor = 0.0
valor2 = 0.0

# Create a for loop to iterate through each row in the xls file, starting from row 2
for r in range(1, sheet.nrows):

    flag = 'S'
    contalinha = contalinha + 1

    codigo = sheet.cell(r,0).value
    descri = sheet.cell(r,1).value
    valor  = sheet.cell(r,3).value
    valor2 = sheet.cell(r,4).value
    registro = codigo[0:12]

    if  descri == '':
        flag = 'N'

    if  valor == '':
        valor = '0.00'
        valor = float(valor)
    if  valor2 == '':
        valor2 = '0.00'
        valor2 = float(valor2)

    if  flag == 'S':
        flag = 'N'
        if  contalinha >= 11 and contalinha <= 13:
            # print('entrei ' + str(contalinha) + ' - ' + registro)
            flag = 'S'
        # if  contalinha >= 22 and contalinha <= 23:
        #     flag = 'S'
        # if  contalinha >= 56 and contalinha <= 72:
        #     flag = 'S'
        # if  contalinha >= 91 and contalinha <= 98:
        #     flag = 'S'
        # if  contalinha >= 119 and contalinha <= 147:
        #     flag = 'S'
        # if  contalinha >= 158 and contalinha <= 172:
        #     flag = 'S'

    if  contalinha  <   20:

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
            verificasetem(registro)

        # print(str(contalinha) + ' --- ' + flag + ' --- ' + str(valor))

    if  flag == 'S':
        contplano = contplano + 1

        tipocd = ''

        if  (codigo[0:1] == '4'):
            tipocd = 'C'

        if  (codigo[0:1] == '3'):
            tipocd = 'D'

        query = 'insert into dbContabil.cadplano (idplano, codigo, descricao, tipocd) values (' + str(contplano) + ',"' + registro + '","' + descri + '","' + tipocd + '")'
        cursor.execute(query)

        contlancto = contlancto + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto, 
            2016, 
            01, 
            registro,
            valor,
            1
            )

        # print query

        # cursor.execute(query)

        contlancto2 = contlancto2 + 1
        query = 'insert into {0}.{1} (idlancamento, ano, mes, idplano, valor, idcliente) values ({2}, {3}, {4}, "{5}", {6}, {7})'.format("dbContabil", "cadlancamento", 
            contlancto2, 
            2015, 
            01, 
            registro,
            valor2,
            1
            )

        cursor.execute(query)

# Close the cursor
cursor.close()

#Commit the transaction
database.commit()
#Close the database connection
database.close()
#Print results
# print “”
print 'Planilha importada com sucesso...'
# print “”
# columns = str(sheet.ncols)
# rows = str(sheet.nrows)
# print "Summary of data imported: " + columns + " columns and " + rows + " rows"
