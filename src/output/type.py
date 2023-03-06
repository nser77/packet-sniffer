from json import dumps

class OutputType:
    @staticmethod
    def json(object):
        return dumps(object, default=lambda object: object.__dict__)
