import codecs
import tornado.web
import json
from database import query

class Handler(tornado.web.RequestHandler):
    
    def set_default_headers(self):
            self.set_header("Access-Control-Allow-Origin", "*")
            self.set_header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
            self.set_header("Access-Control-Allow-Headers",
                            "Content-Type, Depth, User-Agent, X-File-Size, X-Requested-With, X-Requested-By, If-Modified-Since, X-File-Name, Cache-Control")    

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

        result = { 'put': id }

        self.write(result)

    def delete(self, id):

        result = { 'delete': id }

        self.write(result)
