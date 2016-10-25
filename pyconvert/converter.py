from pyconvert import checker
from pyconvert.errors import *
import cmath


class Converter:
    def __init__(self, conversion_type="measurement", convert_from='', convert_to='', parameter=''):
        self.type = conversion_type
        self.convert_from = convert_from
        self.convert_to = convert_to
        self.parameter = parameter
        if not checker.Check(parameter=parameter, convert_from=convert_from, convert_to=convert_to) \
                .is_valid_conversion():
            raise InvalidConversionError("The conversion is invalid")

    def converter(self, relationship):
        if isinstance(relationship, Multiple):
            pass

    def measurement_converter(self):
        pass

    def file_converter(self):
        pass


class Multiple(object):
    pass


