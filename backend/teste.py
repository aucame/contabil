# coding=utf-8

from sqlalchemy import create_engine

# query = 'select count(*) total from dbContabil.cadplano where codigo like "%' + codigo + '%"'
# data = cursor.execute(query)

# print query + str(dir(data))

engine = create_engine('mysql://root:123456@127.0.0.1/dbContabil')
connection = engine.connect()
result = connection.execute("select * from dbContabil.cadplano where codigo = '4.1.1.01.004'")
# result = connection.execute('select * from dbContabil.cadplano')

print result.rowcount

for row in result:
    print("codigo: ", row['codigo'])

connection.close()
