from pickle_database import PickleDatabase

DatabaseFilename = 'PickleDatabase.pickle'


class FileSaveLoad:
    def __init__(self):
        self.allFiles = None

    def load(self):
        self.allFiles = PickleDatabase.loadData(DatabaseFilename)
        return self.allFiles

    def save(self, tags):
        PickleDatabase.saveData(tags, DatabaseFilename)

