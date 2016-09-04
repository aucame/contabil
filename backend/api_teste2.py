#from sqlalchemy import *
#engine = create_engine('mysql://root:123456@200.98.174.103/new_schema?charset=utf8&use_unicode=0', pool_recycle=3600)
#eng = create_engine("mysql://root:123456@200.98.174.103/new_schema",connect_args={"encoding": "utf8"})
#connection = engine.connect()

from sqlalchemy import *

# Let's re-use the same database as before
#db = create_engine('sqlite:///tutorial.db')

engine = create_engine('mysql://root:123456@200.98.174.103/new_schema')

conn = engine.connect()

result = engine.execute("select idnew_table from new_table")

for row in result:
    print "codigo:", row['idnew_table']

result.close()
