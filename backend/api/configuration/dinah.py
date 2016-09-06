from utils import files

class Settings():
    file_utils = files.FileUtils()

    dinah_properties = file_utils.properties('dinah')

    def models_path(self):
        return self.dinah_properties('models_path')

