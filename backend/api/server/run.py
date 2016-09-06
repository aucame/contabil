import tornado.web
from configuration import server
from handlers import default, usuarios

class Web(tornado.web.Application):
    def __init__(self):
        # Endpoints
        #
        # productclustering/column_name/line/(family|family,family,...,family)/clusters/days

        handlers = [
            (r'/',default.Handler),
            (r'/usuarios',usuarios.Handler)
        ]

        tornado.web.Application.__init__(self,handlers)

    def port(self):
        web_settings = server.Settings()

        return web_settings.port()

#            (r'/productclustering/(.*)/(.*)/(.*)/([0-9]+)/([0-9]+)',productclustering.Handler),
#            (r'/block-status/([0-9]+)/([0-9]+)/?([0-9]+)?/?',blockstatus.Handler),
#            (r'/sku_limits/([0-9]+)/?([0-9]+)?/?',skulimits.Handler),
#            (r'/call_prevision/([0-9]+)?/?',callprevision.Handler),
#            (r'/show_process/(.*)',showprocess.Handler)
