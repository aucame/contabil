# coding=utf-8

import xlrd
import MySQLdb

# Open the workbook and define the worksheet
book = xlrd.open_workbook("DRE2016X2015.xls")

sheet = book.sheet_by_name("DRE 2.016 X 2.015")
#sheet = book.sheet_by_index(0)

# Establish a MySQL Connection
database = MySQLdb.connect (host="127.0.0.1", user="root", passwd="123456", db="dbContabil")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

idchave = 0
contador = 0
contlancto = 0

# Create a for loop to iterate through each row in the xls file, starting from row 2
for r in range(1, sheet.nrows):

    codigo = sheet.cell(r,0).value
    descri = sheet.cell(r,1).value
    valor  = sheet.cell(r,3).value
    if  (valor == ''):
        valor = "0.00"
    if  (valor == 'JANEIRO'):
        valor = "0.00"

    if  (codigo[1:2] == '.'):
        registro = codigo[0:12]
        contador = contador + 1

        query = 'insert into dbContabil.cadplano (idplano, codigo, descricao, tipocd) values (' + str(contador) + ',"' + registro + '","' + descri + '","C")'
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

        print query

        cursor.execute(query)



# Close the cursor
cursor.close()

#Commit the transaction
database.commit()
#Close the database connection
database.close()
#Print results
# print “”
# print “Data Imported successfully!!!”
# print “”
# columns = str(sheet.ncols)
# rows = str(sheet.nrows)
# print "Summary of data imported: " + columns + " columns and " + rows + " rows"
