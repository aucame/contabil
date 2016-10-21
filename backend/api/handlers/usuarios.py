import codecs
import tornado.web
import json
from database import query

class Handler(tornado.web.RequestHandler):
    
    def set_default_headers(self):
        #self.set_header("Access-Control-Allow-Credentials", "true")
        #self.set_header("Access-Control-Allow-Origin", "*")
        #self.set_header("Access-Control-Allow-Methods", "GET, PUT, POST, DELETE, OPTIONS")
        #self.set_header("Access-Control-Request-Methods", "Origin, X-Request-Width, Content-Type, Accept")
        #self.set_header("Access-Control-Allow-Headers" "Origin") #, X-Requested-With, Content-Type, Accept")

        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, Content-Type, application/json")
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

        data = { "idusuario": int(id) }

        db_execute = query.MySqlQuery()
        result = db_execute.deleta_usuario(data)

        self.write(data)

    def options(self, id):
    
        print('passou no options')
        # no body
        self.set_status(200)
    #    self.finish()
