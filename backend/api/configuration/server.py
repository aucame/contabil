from utils import files

class Settings():
    file_utils = files.FileUtils()

    server_properties = file_utils.properties('server')

    def port(self):
        return int(self.server_properties['port'])
