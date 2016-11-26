import codecs
import tornado.web
import json
from database import dblancamento

class Handler(tornado.web.RequestHandler):
    
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, Content-Type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE, OPTIONS')        

    def get(self, id):
        db_execute = dblancamento.MySqlQuery()
        result = db_execute.get_registro(id)
        self.write(result)

    def post(self, id):
        data = self.request.body
        db_execute = dblancamento.MySqlQuery()
        result = db_execute.cria_registro(data)
        self.write(data)

    def put(self, id):
        data = self.request.body
        db_execute = dblancamento.MySqlQuery()
        result = db_execute.altera_registro(data)
        self.write(data)

    def delete(self, id):
        db_execute = dblancamento.MySqlQuery()
        result = db_execute.deleta_registro(id)
        self.write(id)

    def options(self, id):
        self.set_status(200, "OK")
        self.finish()
