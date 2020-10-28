import configparser
import os

config_file = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', "config.ini"))

class Config:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_config(self, category, name):
        try:
            value = self.config[category][name]
            return int(value)
        except ValueError:
            return value
        except KeyError:
            print("Chave não existe")

