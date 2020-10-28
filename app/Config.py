import configparser

class Config:

    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_config(self, category, name):
        return self.config[category][name]
