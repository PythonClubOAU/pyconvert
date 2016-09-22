from pyconvert import base


def is_type_valid(self):
        if not isinstance(self, str):
            raise TypeError("The name {0} is not of type str. All unit entered must be strings".format(self))
        else:
            return True


def is_name_valid(value, self="measurement"):
        if value in base.conversion_dict[self].keys():
            return True
        elif value not in base.conversion_dict[self].keys():
            for key, values in base.conversion_dict[self].items():
                if value in values["available_units"]:
                    return False
                else:
                    return True



is_name_valid("g")