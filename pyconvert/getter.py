from pyconvert import base, validator, checker
from pyconvert.errors import *
import tabulate
"""
    Getter Class.
    Would perform basic getting functions.
    Get some values based on provided keywords.
    Could be used as a quick reference library.
    """



def get_unit_details_from_name(value, type="measurement"):
        """
        Get the unit of a measurement value by providing its name.\n
        \n:params:
        \nvalue: has to be of type str
        \nname:has to be of type str
        \ntype:Optional(If specified, it has to be either of type mathematical or files)
        \n:return: Details about the given unit.
        \n:errors: TypeError
        """
        if validator.is_type_valid(value) and validator.is_name_valid(value):
            unit = base.conversion_dict[type][value]["standard_unit"]
            return unit
        else:
            raise UnitError("The unit {0} is not a valid unit or it does not exist.".format(value))


def get_name_from_unit(unit, type="measurement"):
        """
                Get the name of a measurement value by providing its unit.
                :param value:has to be of type str
                :param name:has to be of type str
                :param type:Optional(If specified, it has to be either of type mathematical or files)
                :return: Details about the given unit.
                :errors: TypeError
                """

        if validator.is_type_valid(unit) and validator.is_name_valid(unit):
                for key, values in base.conversion_dict[type].items():
                    if unit in values["available_units"]:
                        print("Nope")
                        return False
                else:
                    return True

                exit()
                units = base.conversion_dict[type][unit]
                for keys, values in base.conversion_dict.items():
                    # @Todo : Finish this by returning correct response...
                    print(keys, values)
        else:
                raise UnitError("The unit {0} is not a valid unit.".format(unit))



def get_table_for_unit(self, type="measurement"):
        # @Todo: Get tabulate for tables...
        # @Todo: Might need to move this to a Tables class later on..*[absc]:

        """
        Return a 2D tabular representation of a unit conversions variable.
        Makes use of the tabulate module
        :param:to_return
        :return:
        """
        # @Todo: Reformat all table values.
        if not self in base.conversion_dict[type]:
            raise IndexError("Invalid name is specified")
        else:
            to_tabulate = base.conversion_dict[type][self]
            print(tabulate.tabulate(to_tabulate,
                                    headers=[
                                        ['standard_symbol', 'standard_unit', 'available_units', 'available_converts',
                                         'converts_and_units']]))


def get_table_for_all_measurement():
        """
        Returns a 2D tabular representation of all units conversion variables available.
        Also uses tabulate
        :rtype: object
        :return:
        """
        # @Todo: Reformat all table values.
        for key, value in base.conversion_dict.items():
            print(tabulate.tabulate([key, value]))


def get_file_type(name, type="file"):
        if checker.is_valid_file(name):
            pos = name.find(".")
            position = name[(pos + 1):]
            if not position in base.conversion_dict[type]["file_type"]:
                raise TypeError("Your file has an invalid or unsupported extension")
            else:
                file_type = base.conversion_dict[type]["base_symbols"]
                for key, val in file_type.items():
                    if position in val:
                        return file_type
                    else:
                        raise TypeError("Your file has an invalid or unsupported extension")


get_name_from_unit("m")
