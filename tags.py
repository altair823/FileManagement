from file_schema import FileSchema
from file_exception import WrongClassException, ExistedFilenameException
from datetime import datetime


class Tags:
    def __init__(self):
        self.files = dict()
        self.lastUpdateTime = 0

    def insertNewFile(self, fileSchema):
        if type(fileSchema) != FileSchema:
            raise WrongClassException
        elif fileSchema.filename in self.files:
            raise ExistedFilenameException
        else:
            self.files[fileSchema.path] = fileSchema
            self.lastUpdateTime = datetime.now()

    def __str__(self):
        tagsStr = ''
        for key in self.files.keys():
            tagsStr += str(self.files[key])
            tagsStr += '\n'
        return tagsStr
