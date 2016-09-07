import codecs
import tornado.web
from database import query

class Handler(tornado.web.RequestHandler):
    def get(self):

        db_execute = query.MySqlQuery()
        result = db_execute.get_usuarios()
        self.set_header('Access-Control-Allow-Origin','*')
        self.set_header('Content-Type','application/json')

       	#self.write(db_execute.getLimitesSku(subcategory_id, branch_id))
        self.write(result)
