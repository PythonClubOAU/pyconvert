from pyconvert import base, errors


class Checker:
    def get_unit_details_from_name(value, name="measurement"):
        """
        Get the unit of a measurement value by providing its name.
        :param value:has to be of type str
        :param name:has to be of type str
        :param type:Optional(If specified, it has to be either of type mathematical or files)
        :return: Details about the given unit.
        :errors: TypeError
        """
        if base.Validator.is_type_valid(value):
                if base.Validator.is_name_valid(name, value):
                    unit = base.__all__[name][value]
                    print(unit)
                    return unit
                else:
                    raise errors.UnitError("The unit {0} is not a valid unit.".format(value))
        else:
                raise TypeError

    def get_table_for_unit(self, type="measurement"):
        # @Todo: Get tabulate for tables
        """
        Return a 2D tabular representation of a unit conversions variable.
        Makes use of the tabulate module
        :param:to_return
        :return:
        """

    def get_table_for_all_unit(self="measurement"):
        """
        Returns a 2D tabular representation of all units conversion variables available.
        Also uses tabulate
        :return:
        """

    def if_conversion_is_valid(self, paremeter, convert_from, convert_to, type="measurement"):
        """
         :param self: unit
         :param convert_to: unit to convert from
         :param parameter: parameter to be checked. Should be either name or symbol
        :param convert_from: unit to convert from
        :param type: measurement by default
        :return: True if conversion is allowed and False if not
        """
        if not self in base.__all__[type]:
            raise IndexError("Invalid name is specified")
        else:
            if paremeter not in ["name", "symbol"]:
                    raise IndexError("The provided parameter is invalid")
            elif paremeter == "name":
                    if convert_from and convert_to in base.__all__[type][self]["available_converts"]:
                        return True
                    else:
                        return False

check = Checker
check.if_conversion_is_valid("speed", paremeter="name", convert_from="metres_per_second", convert_to="kilometer_per_second")
