from file_schema import FileSchema
from tags import Tags
from file_exception import WrongClassException
from os import path
import os


def MakeFileSchema(filePath):
    if path.isfile(filePath) or path.isdir(filePath) or \
            path.isfile(path.abspath(filePath)) or path.isdir(path.abspath(filePath)):
        newFileSchema = FileSchema()
        if path.isabs(filePath):
            newFileSchema.filename = path.basename(filePath)
            newFileSchema.path = filePath
            newFileSchema.parent = path.dirname(filePath)
            if path.isfile(filePath):
                newFileSchema.isfile = True
            else:
                newFileSchema.isfile = False
            newFileSchema.stat = os.stat(filePath)
        else:
            newFileSchema.filename = filePath
            newFileSchema.path = path.abspath(filePath)
            newFileSchema.parent = path.dirname(path.abspath(filePath))
            if path.isfile(path.abspath(filePath)):
                newFileSchema.isfile = True
            else:
                newFileSchema.isfile = False
            newFileSchema.stat = os.stat(path.abspath(filePath))
        return newFileSchema
    else:
        raise FileNotFoundError


def MakeFileSchemaFromLootDir(dirPath, tags):
    if not path.isdir(dirPath):
        return MakeFileSchema(dirPath)
    if type(tags) != Tags:
        raise WrongClassException
    if dirPath in tags.files and os.path.getmtime(dirPath) <= tags.files[dirPath].stat.st_mtime:
        return


    Queue = [dirPath]
    currentLoot = path.abspath(dirPath)
    currentFileList = os.listdir(dirPath)

    for i in range(len(currentFileList)):
        currentFileList[i] = currentLoot + '\\' + currentFileList[i]


    Queue += currentFileList

    for file in Queue:
        print(file)
        if file in tags.files and os.path.getmtime(file) <= tags.files[file].stat.st_mtime:
            continue
        newFSCH = MakeFileSchema(file)
        tags.insertNewFile(newFSCH)
        if path.isdir(file):
            tempQueue = os.listdir(file)
            for i in range(len(tempQueue)):
                tempQueue[i] = file + '\\' + tempQueue[i]
            Queue += tempQueue


