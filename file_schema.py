

class FileSchema:
    def __init__(self):
        self.filename = ''
        self.path = ''
        self.parent = ''
        self.isfile = None
        self.tag = set()
        self.stat = None
        self.updateTime = 0

    def __str__(self):
        return self.filename + ': ' + str(self.tag) + ' - isfile: ' + str(self.isfile) + ' - ' + str(self.stat)
