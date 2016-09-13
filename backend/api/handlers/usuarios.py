import codecs
import tornado.web
from database import query

class Handler(tornado.web.RequestHandler):

    def get(self, id):

        db_execute = query.MySqlQuery()
        result = db_execute.get_usuarios(id)
        
        self.set_header('Access-Control-Allow-Origin','*')
        self.set_header('Content-Type','application/json')

       	#self.write(db_execute.getLimitesSku(subcategory_id, branch_id))
        self.write(result)

    def post(self, id):
    
        self.set_header('Access-Control-Allow-Origin','*')
        self.set_header('Content-Type','application/json')

        result = { 'post': id }

        result = self.request.body

        self.write(result)

    def put(self, id):

        self.set_header('Access-Control-Allow-Origin','*')
        self.set_header('Content-Type','application/json')

        result = { 'put': id }

        self.write(result)

    def delete(self, id):

        self.set_header('Access-Control-Allow-Origin','*')
        self.set_header('Content-Type','application/json')

        result = { 'delete': id }

        self.write(result)
