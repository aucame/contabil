import tornado.httpserver
#from server import run

def main():
    application_server = run.Web()

    http_server = tornado.httpserver.HTTPServer(application_server)
    http_server.bind(application_server.port())
    http_server.start(0)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
