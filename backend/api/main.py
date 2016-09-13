import tornado.httpserver
from server import run

def main():
    
    print('Servidor iniciado localhost:8080')

    application_server = run.Web()

    http_server = tornado.httpserver.HTTPServer(application_server)
    http_server.bind(application_server.port())
    http_server.start(0)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()


# sudo apt-get install python-dev libmysqlclient-dev  -- Precisa instalar esses pacotes para acesso ao mysql com sqlalchemy
# pip install mysql-python
