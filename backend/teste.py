# -*- coding: utf-8 -*-

import MySQLdb
from sqlalchemy import create_engine

# from sqlalchemy import create_engine

# # query = 'select count(*) total from dbContabil.cadplano where codigo like "%' + codigo + '%"'
# # data = cursor.execute(query)

# # print query + str(dir(data))

# engine = create_engine('mysql://root:123456@127.0.0.1/dbContabil')
# connection = engine.connect()
# result = connection.execute("select * from dbContabil.cadplano where codigo = '2.1.1.03.004'")
# # result = connection.execute('select * from dbContabil.cadplano')

# print result.rowcount

# for row in result:
#     print("codigo: ", row['codigo'])

# connection.close()

# import fpdf

# pdf = fpdf.FPDF(format='A4')
# pdf.add_page()
# pdf.set_font("Arial", size=10)
# pdf.cell(10, 10, txt="Welcome to Python!", align="L")
# pdf.cell(10, 20, txt="Welcome to Python!", align="L")
# pdf.cell(70, 20, txt="Welcome to Python!", align="L")
# pdf.output("tutorial.pdf")

# html = """
# <H1 align="center">html2fpdf</H1>
# <h2>Basic usage</h2>
# <p>You can now easily print text while mixing different
# styles : <B>bold</B>, <I>italic</I>, <U>underlined</U>, or
# <B><I><U>all at once</U></I></B>!

# <BR>You can also insert hyperlinks
# like this <A HREF="http://www.mousevspython.com">www.mousevspython.com</A>,
# or include a hyperlink in an image. Just click on the one below.<br>
# <center>
# <A HREF="http://www.mousevspython.com"></A>
# </center>

# <h3>Sample List</h3>
# <ul><li>option 1</li>
# <ol><li>option 2</li></ol>
# <li>option 3</li></ul>

# <table border="0" align="center" width="50%">
# <thead><tr><th width="30%">Header 1</th><th width="70%">header 2</th></tr></thead>
# <tbody>
# <tr><td>cell 1</td><td>cell 2</td></tr>
# <tr><td>cell 2</td><td>cell 3</td></tr>
# </tbody>
# </table>
# """

# from fpdf import FPDF, HTMLMixin

# class MyFPDF(FPDF, HTMLMixin):
#     pass

# pdf=MyFPDF()
# #First page
# pdf.add_page()
# pdf.write_html(html)
# pdf.output('html.pdf','F')



# Establish a MySQL Connection
ipservidor = "127.0.0.1" # LOCAL
# ipservidor = "200.98.174.103" # UOLHOST

usuario    = "root"
# senha      = "lelo$321"
senha      = "123456"
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
    print '|' + row[0] + '|' + row[1] + '|' + str(row[2]) + '|' + str(row[3]) + '|' + str(row[4]) + '|'

cursor.close()
connection.close()
