# coding=utf-8

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

# pdf = fpdf.FPDF(format='letter')
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# pdf.cell(200, 10, txt="Welcome to Python!", align="C")
# pdf.output("tutorial.pdf")

html = """
<H1 align="center">html2fpdf</H1>
<h2>Basic usage</h2>
<p>You can now easily print text while mixing different
styles : <B>bold</B>, <I>italic</I>, <U>underlined</U>, or
<B><I><U>all at once</U></I></B>!

<BR>You can also insert hyperlinks
like this <A HREF="http://www.mousevspython.com">www.mousevspython.com</A>,
or include a hyperlink in an image. Just click on the one below.<br>
<center>
<A HREF="http://www.mousevspython.com"></A>
</center>

<h3>Sample List</h3>
<ul><li>option 1</li>
<ol><li>option 2</li></ol>
<li>option 3</li></ul>

<table border="0" align="center" width="50%">
<thead><tr><th width="30%">Header 1</th><th width="70%">header 2</th></tr></thead>
<tbody>
<tr><td>cell 1</td><td>cell 2</td></tr>
<tr><td>cell 2</td><td>cell 3</td></tr>
</tbody>
</table>
"""

from fpdf import FPDF, HTMLMixin

class MyFPDF(FPDF, HTMLMixin):
    pass

pdf=MyFPDF()
#First page
pdf.add_page()
pdf.write_html(html)
pdf.output('html.pdf','F')