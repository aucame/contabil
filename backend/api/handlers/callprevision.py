import codecs
import tornado.web
from utils import commands

class Handler(tornado.web.RequestHandler):
    def get(self, category_id):
        result = {}
        cm_execute = commands.Prevision()

        self.set_header('Access-Control-Allow-Origin','*')
        self.set_header('Content-Type','application/json')

       	self.write(cm_execute.executar(category_id))
