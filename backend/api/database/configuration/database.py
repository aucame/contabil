from utils import files
# import ConfigParser

class Settings():
    file_utils = files.FileUtils()
    database_properties = ""

    def setDatabase(self, database):
        self.database_properties = self.file_utils.properties(database)

    def port(self):
        return int(self.database_properties['port'])

    def host(self):
        return self.database_properties['host']

    def user(self):
        return self.database_properties['user']

    def password(self):
        return self.database_properties['password']

    def database(self):
        return self.database_properties['database']