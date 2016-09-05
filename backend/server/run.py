import tornado.web
from configuration import server
from handlers import *

class Web(tornado.web.Application):
    def __init__(self):
        # Endpoints
        #
        # productclustering/column_name/line/(family|family,family,...,family)/clusters/days

        handlers = [
            (r'/usuarios/(.*)/(.*)/(.*)/([0-9]+)/([0-9]+)',Usuarios.Handler)
        ]

        tornado.web.Application.__init__(self,handlers)

    def port(self):
        web_settings = server.Settings()

        return web_settings.port()
