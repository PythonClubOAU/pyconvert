from pyconvert import base,  checker
from pyconvert.errors import *
import tabulate


class Get:
    def __init__(self, value, conversion_type='measurement', unit=''):
        self.value = value
        self.unit = unit
        self.type = conversion_type
        if checker.Check.is_type_valid(value) and checker.Check().is_name_valid():
            self.unit = base.conversion_dict[self.type][value]["standard_unit"]
        else:
            raise UnitError("The unit {0} is not a valid unit or it does not exist.".format(value))

    def unit_from_value(self):
        return self.unit

    def name_from_unit(self, unit):
        if unit not in base.conversion_dict[self.type][self.value]["converts_and_units"].values():
            raise UnitError("The unit {0} is not a valid unit.".format(unit))
        else:
            return unit

    def table_for_unit(self):
        if self.unit not in base.conversion_dict[self.type]:
            raise UnitError("Invalid name is specified")
        else:
            to_tabulate = base.conversion_dict[type][self]
            print(tabulate.tabulate(to_tabulate, headers=['standard_symbol', 'standard_unit', 'available_units',
                                                         'available_converts',
                                                 'converts_and_units']))

    def table_for_all_measurement(self):
        for key, value in base.conversion_dict.items():
            print(tabulate.tabulate([key, value]))

test = Get(value="temperature")
print(test.name_from_unit('L'))
