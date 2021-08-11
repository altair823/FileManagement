import os
from pickle import dump, load
from tags import Tags
from file_exception import WrongClassException


class PickleDatabase:
    @staticmethod
    def saveData(allData, DatabaseFilename):
        if type(allData) != Tags:
            raise WrongClassException
        else:
            with open(DatabaseFilename, 'wb') as database:
                dump(allData, database)

    @staticmethod
    def loadData(DatabaseFilename):
        try:
            with open(DatabaseFilename, 'rb') as database:
                tempData = load(database)
            return tempData
        except FileNotFoundError:
            print('There is no pickle file. Make a new one.')
            with open(DatabaseFilename, 'wb') as database:
                print('Made new pickle file named ' + DatabaseFilename + 'at ' + os.path.abspath(DatabaseFilename))
            return Tags()
        except EOFError:
            return Tags()
