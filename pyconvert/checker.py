from pyconvert import base,getter
import os


def conversion_is_valid(self, convert_from, convert_to, parameter="symbol", type="measurement"):
        """
             :param self: name
             :param convert_to: unit to convert from
             :param parameter: parameter to be checked. Should be either name or symbol
            :param convert_from: unit to convert from
            :param type: measurement by default
            :return: True if conversion is allowed and False if not
            """
        # @Todo: Get unit if name is not valid and validate conversion with the unit.
        # if not name:
        # unit = Getter.get_name_from_unit(convert_from)
        if not self in base.conversion_dict[type]:
            raise IndexError("Invalid name is specified")
        else:
            if parameter not in ["name", "symbol"]:
                raise IndexError("The provided parameter is invalid")
            elif parameter == "name":
                if convert_from and convert_to in base.conversion_dict[type][self]["available_converts"]:
                    return True
                else:
                    return False
            elif parameter == "symbol":
                if convert_from and convert_to in base.conversion_dict[type][self]["available_units"]:
                    return True
                else:
                    return False

def unit_is_valid(self, unit, type="measurement"):
        """
            Check if a provided unit for a quantity is valid.
            Return true if valid and false if not.
            :param unit: quantity to check unit for
            :param self: unit to check
            :param type: measurement by default.
            :return:
            """
        if not self in base.conversion_dict[type]:
            raise IndexError("Invalid name is specified")
        else:
            if unit in base.conversion_dict[type]["available_units"] and unit != base.conversion_dict[type]["standard_unit"]:
                print("The specified unit is available for the {0} but is not the standard unit.")
            elif unit in base.conversion_dict[type]["available_units"] and unit == base.conversion_dict[type]["standard_unit"]:
                return True
            else:
                return False

def is_valid_path(path, type="file"):
        """
            Extension checking class.
            Would check if the provided extension for a file name is valid or not.
            Provide the file name in any two ways.
            filename with extension or specify the extension separately.
            For example:
            a = Checker.FileChecker.extension_is_valid(filename="test.txt") or
            a = Checker.FileChecker.extension_is_valid(filename_without_ext="test", extension= "txt")
            :param filename:
            :return: True if it is. False if not.
            """
        if not type:
            raise TypeError("Invalid Type specified")
        else:
            if not os.path.isfile(path):
                is_valid = False
                return is_valid
            else:
                return True


def is_valid_file(self, type="file"):
        if not type:
            raise TypeError("Invalid Type specified")
        else:
            if getter.get_file_type(self):
                return True
            else:
                return False
