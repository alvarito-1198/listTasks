import configparser
import io
import os

class Config:

    def __init__(cls):
        cls.__config = configparser.ConfigParser()
        # Read the configuration file
        cls.__config.read('config.ini')
        # Access values from the configuration file
        cls.__database = cls.__config.get('sqlite', 'name_db')

    def read_value(cls, section, key ):
        return cls.__config.get(section,key)

    def list_values(cls):
        print("List all contents")
        for section in cls.__config.sections():
            print("Section: %s" % section)
            for options in cls.__config.options(section):
                print("x %s:::%s:::%s" % (options,
                                          cls.__config.get(section, options),
                                          str(type(options))))

