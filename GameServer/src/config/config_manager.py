# ======================================================================
# Function: Manage config
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):

    def __init__(self):
        self.name = ''

    def start_element(self, name, attrs):
        self.name = str(name)

    def end_element(self, name):
        pass

    def char_data(self, text):
        if self.name == 'db_file':
            ConfigManager.DB_file = str(text)

class ConfigManager(object):

    config_file = '../config.xml'
    DB_file = ''

    @classmethod
    def init(cls):
        handler = DefaultSaxHandler()
        parser = ParserCreate()
        parser.StartElementHandler = handler.start_element
        parser.EndElementHandler = handler.end_element
        parser.CharacterDataHandler = handler.char_data

        with open(cls.config_file, 'r') as f:
            s = str(f.read())
            s = s.replace('\n', '')
            parser.Parse(s)
