from pyconvert import base


class UnitError(Exception):
    def __init__(self, error_message):
        self.error_message = error_message
        print(self.error_message)
