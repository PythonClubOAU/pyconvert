from pyconvert import base
import os


class Check:
    def __init__(self, name='', convert_from='', convert_to='', parameter="symbol", conversion_type="measurement",
                 unit='',
                 path=''):
        self.name = name
        self.parameter = parameter
        self.convert_from = convert_from
        self.convert_to = convert_to
        self.conversion_type = conversion_type
        self.unit = unit
        self.path = path
        if self.conversion_type not in base.conversion_dict.keys():
            raise IndexError("Invalid name is specified")

    def is_valid_conversion(self):
        if self.parameter not in ["name", "symbol"]:
            raise Check("The provided parameter is invalid.")
        elif self.parameter == "name":
            if self.convert_from and self.convert_to in base.conversion_dict[self.conversion_type][self][
                    "available_converts"]:
                return True
            else:
                return False
        elif self.parameter == "symbol":
            if self.convert_from and self.convert_to in base.conversion_dict[self.conversion_type][self][
                    "available_units"]:
                return True
            else:
                return False

    def is_valid_unit(self):
        if self.unit in base.conversion_dict[self.conversion_type]["available_units"] and self.unit != \
                base.conversion_dict[self.conversion_type][
                    "standard_unit"]:
            print("The specified unit is available for the {0} but is not the standard unit.")
            return True
        elif self.unit in base.conversion_dict[self.conversion_type]["available_units"] and self.unit == \
                base.conversion_dict[self.conversion_type][
                    "standard_unit"]:
            return True
        else:
            return False

    def is_valid_path(self):
        if not self.conversion_type == "files":
            raise Exception("Invalid Type specified")
        file = self.path[(self.path.rfind('/') + 1):]
        path = self.path[:self.path.find(file)]
        if not os.path.isdir(path):
            return False
        else:
            return file

    def is_valid_file(self):
        file = self.is_valid_path()
        if file:
            return True
        else:
            raise Exception("The specified path is not valid.")

    def is_type_valid(self):
        if not isinstance(self.name, str):
            raise TypeError("The name {0} is not of type str. All unit entered must be strings".format(self))
        else:
            return True

    def is_name_valid(self):
        if self.name in base.conversion_dict[self.conversion_type].keys():
            return True
        elif self.name not in base.conversion_dict[self].keys():
            for key, values in base.conversion_dict[self].items():
                if self.name in values["available_units"]:
                    return False
                else:
                    return True
