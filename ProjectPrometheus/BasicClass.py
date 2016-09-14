__author__ = 'I067382'


from BasicFunc import *


class DB(object):
    def __init__(self, dbJsonFileLoc=''):
        self.dbJsonFileLoc = dbJsonFileLoc

    def getDBAttribute(self):
        attributeJsonObject = getJsonObject(self.dbJsonFileLoc)
        return attributeJsonObject['DBAttribute']

    def install(self): pass


