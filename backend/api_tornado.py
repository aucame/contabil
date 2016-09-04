import tornado.ioloop
import tornado.web

def teste():
    bla = 'teste'
    return bla

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        retorno = teste()
        registro = []

        self.write(retorno)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
