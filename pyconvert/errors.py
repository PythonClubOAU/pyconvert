
class UnitError(Exception):
    def __init__(self, error_message):
        self.error_message = error_message
        print(self.error_message)


class NotValidError(Exception):
    def __init__(self, error_message):
        self.error_mesage = error_message
        print(self.error_mesage)


class NotValidTypeError(Exception):
    def __init__(self, error_message):
        self.error_mesage = error_message
        print(self.error_mesage)

class VersionError(Exception):
    def __init__(self, error_message):
        self.error_mesage = error_message
        print(self.error_mesage)