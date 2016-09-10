import codecs
import tornado.web

class Handler(tornado.web.RequestHandler):
    def get(self, id):

        result = { 'codigo': id }

        self.set_header('Access-Control-Allow-Origin','*')
        self.set_header('Content-Type','application/json')

        self.write(result)
