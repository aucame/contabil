import codecs
import tornado.web
import json
from database import query

class Handler(tornado.web.RequestHandler):
    
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, Content-Type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE, OPTIONS')        

    def get(self, id):
        db_execute = query.MySqlQuery()
        result = db_execute.get_usuarios(id)
        self.write(result)

    def post(self, id):
        data = self.request.body
        db_execute = query.MySqlQuery()
        result = db_execute.cria_usuario(data)
        self.write(data)

    def put(self, id):
        data = self.request.body
        db_execute = query.MySqlQuery()
        result = db_execute.altera_usuario(data)
        self.write(data)

    def delete(self, id):
        db_execute = query.MySqlQuery()
        result = db_execute.deleta_usuario(id)
        self.write(id)

    def options(self, id):
        self.set_status(200, "OK")
        self.finish()
