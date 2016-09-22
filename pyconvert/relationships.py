from pyconvert import base, errors

all_values = base.conversion_dict


class Length:
    """
    Base Class defining all relationships between length measurement variables.
    Is heavily dependent upon by whole project.
    Internationalization has not been implemented yet.
    All units are US based now.
    !!!!!PLEASE!!!!!!
    Do not edit until you've spoken to me
    !!!!!PLEASE!!!!!
    """

    def metres(self, convert_from, convert_to):
        units = base.conversion_dict["measurement"]["length"]["available_converts"]
        if not self in units:
            raise errors.UnitError("The specified unit is not valid.")
        else:
            metres = 100
            centimetres = metres * 100
            decimeters = metres * 10
            millimeters = ""
            kilometers = metres * 1000
            miles = ""
            inches = ""
            foot = ""
            lengths = [metres, centimetres, decimeters, millimeters, kilometers,miles, inches, foot]


    def volume(self):
        pass

    def pressure(self):
        pass

    def temperature(self):
        pass

    def mass(self):
        pass

    def currency(self):
        pass


class Files:
    def __init__(self):
        pass

Length.metres('metres', 'metres', 'centimetres')