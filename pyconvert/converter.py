from pyconvert import base, errors
import tabulate


class Getter:
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
        if base.Validator.is_type_valid(value):
            if base.Validator.is_name_valid(type, value):
                unit = base.__all__[type].keys()
                print(unit)
                return unit
            else:
                raise errors.UnitError("The unit {0} is not a valid unit.".format(value))
        else:
            raise TypeError

    def get_name_from_unit(unit, type="measurement"):
        """
                Get the name of a measurement value by providing its unit.
                :param value:has to be of type str
                :param name:has to be of type str
                :param type:Optional(If specified, it has to be either of type mathematical or files)
                :return: Details about the given unit.
                :errors: TypeError
                """
        if base.Validator.is_type_valid(unit):
            if base.Validator.is_name_valid(type, unit):
                print(base.__all__[type]["hi"])
                exit()
                units = base.__all__[type][unit]
                for keys, values in base.__all__.items():
                    # @Todo : Finish this by returning correct response...
                    print(keys, values)
            else:
                raise errors.UnitError("The unit {0} is not a valid unit.".format(unit))
        else:
            raise TypeError

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
        if not self in base.__all__[type]:
            raise IndexError("Invalid name is specified")
        else:
            to_tabulate = base.__all__[type][self]
            print(tabulate.tabulate(to_tabulate,
                                    headers=[
                                        ['standard_symbol', 'standard_unit', 'available_units', 'available_converts',
                                         'converts_and_units']]))

    @staticmethod
    def get_table_for_all_measurement():
        """
        Returns a 2D tabular representation of all units conversion variables available.
        Also uses tabulate
        :rtype: object
        :return:
        """
        # @Todo: Reformat all table values.
        for key, value in base.__all__.items():
            print(tabulate.tabulate([key, value]))


class Checker:
    """"
    Base class for all checks before converting.
    """

    class MathMeasurementChecker:
        def __init__(self):
            pass

        def conversion_is_valid(name, convert_from, convert_to, parameter="symbol", type="measurement"):
            """
             :param name: name
             :param convert_to: unit to convert from
             :param parameter: parameter to be checked. Should be either name or symbol
            :param convert_from: unit to convert from
            :param type: measurement by default
            :return: True if conversion is allowed and False if not
            """
            # @Todo: Get unit if name is not valid and validate conversion with the unit.
            # if not name:
            # unit = Getter.get_name_from_unit(convert_from)
            if not name in base.__all__[type]:
                raise IndexError("Invalid name is specified")
            else:
                if parameter not in ["name", "symbol"]:
                    raise IndexError("The provided parameter is invalid")
                elif parameter == "name":
                    if convert_from and convert_to in base.__all__[type][name]["available_converts"]:
                        return True
                    else:
                        return False
                elif parameter == "symbol":
                    if convert_from and convert_to in base.__all__[type][name]["available_units"]:
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
            if not self in base.__all__[type]:
                raise IndexError("Invalid name is specified")
            else:
                if unit in base.__all__[type]["available_units"] and unit != base.__all__[type]["standard_unit"]:
                    print("The specified unit is available for the {0} but is not the standard unit.")
                elif unit in base.__all__[type]["available_units"] and unit == base.__all__[type]["standard_unit"]:
                    return True
                else:
                    return False

    class FileChecker:
        """
        Base class for checking files before conversion.
        Its highly depended on by the Converter.FileConverter method.
        Could be called alone or subclassed by a class.
        """

        def __init__(self, type="files"):
            self.type = type

        def extension_is_valid(filename, filename_without_ext="", extension=""):
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


class Converter:
    """
    Main converter class.
    Would take care of all conversions.
    All types.
    """

    def __init__(self, type="measurement"):
        self.type = type

    class QuickConvert:
        """
        This would take care of quickly making quick simple conversions.
        It should be called when the conversion varibles need to be passed straight through a class.
        """

        def __init__(self, convert_from, convert_to, type="measurement"):
            self.type = type
            self.convert_to = convert_to
            self.conver_from = convert_from
            if Checker.MathMeasurementChecker.conversion_is_valid():
                pass

    class MeasurementConverter:
        """
        This would take care of all measurement based conversions.
        All other unit based conversions would subclass this function.
        Would most likely be called in two ways.
        Pass the variables straight through the class or subclass the specific measurement variables you want.
        Passing variables through the class would use QuickConvert.
        :return:

        Example:
        convert = Converter.Measurement_converter()
        """

        def __init__(self, name, parameter, convert_from, convert_to, type="measurement"):
            self.name = name
            self.convert_from = convert_from
            self.convert_to = convert_to
            self.type = type
            self.parameter = parameter
            if Checker.MathMeasurementChecker.conversion_is_valid(name, parameter, convert_to, convert_from):
                pass

    class FileConverter:
        """
        Base file conversion class.

        """
        pass
