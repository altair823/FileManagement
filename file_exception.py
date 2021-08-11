class WrongClassException(Exception):
    def __init__(self, msg='', arg=()):
        self.args = arg
        self.msg = msg

    def __str__(self):
        return 'Wrong Class Exception occurs! ' + self.msg + self.args[0]


class ExistedFilenameException(Exception):
    def __init__(self, msg='', arg=()):
        self.args = arg
        self.msg = msg

    def __str__(self):
        return 'The File is already existed in tag class! ' + self.msg + self.args[0]

class ExistedTagException(Exception):
    def __init__(self, msg='', arg=()):
        self.args = arg
        self.msg = msg

    def __str__(self):
        return 'The Tag is already existed in tag list! ' + self.msg + self.args[0]
