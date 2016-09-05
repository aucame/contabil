import codecs
import tornado.web
from database import query

class Handler(tornado.web.RequestHandler):
    def get(self, subcategory_id, branch_id=False):
        result = {}
        db_execute = query.OracleQuery()

        self.set_header('Access-Control-Allow-Origin','*')
        self.set_header('Content-Type','application/json')

       	self.write(db_execute.getLimitesSku(subcategory_id, branch_id))
