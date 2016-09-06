"""
Base PyConvert class.
Contains all measurements and their likely conversions, all files and their likely extensions and
"""
import dbm


__all__ = dict(measurement=dict(
    length=dict(standard_unit="m", standard_symbol="m", available_converts=["metres",
                                                                            "centimeter", "millimeter",
                                                                            "decimeter", "kilometer",
                                                                            "miles", "inches", "foot"],
                available_units=["m", "cm", "mm", "dm", "km", "mi", "in", "ft"],
                converts_and_units={"metres": "m", "centimetre": "cm", "millimeter": "mm",
                                    "decimeter": "dm", "kilometer": "km", "miles": "mi",
                                    "inches": "in", "foot": "ft"}),
    mass=dict(standard_unit="gramme", standard_symbol="g", available_converts=["grammes",
                                                                               "kilogrammes",
                                                                               "pounds"],
              available_units=["g", "kg", "p"],
              converts_and_units={"grammes": "g", "kilogrammes": "kg", "pounds": "p"}),
    volume=dict(standard_unit="m3", standard_symbol="V", available_converts=["metre_cube",
                                                                             "centimetre_cube",
                                                                             "millimeter_cube",
                                                                             "kilometer_cube"],
                available_units=["m3", "cm3", "mm3", "km3"],
                converts_and_units={"metre_cube": "m3", "centimetre_cube": "cm3",
                                    "millimeter_cube": "mm3", "kilometer_cube": "km3"}),
    speed=dict(standard_unit="m/s", standard_symbol="m/s", available_converts=[
        "metres_per_second",
        "centimetre_per_second", "millimeter_per_second",
        "decimeter_per_second", "kilometer_per_second"],
               available_units=["m/s", "mm/s", "dm/s", "cm/s", "km/hr"],
               converts_and_units={"metres_per_second": "m/s", "centimetre_per_second": "cm/s",
                                   "millimeter_per_second": "mm/s",
                                   "decimeter_per_second": "dm/s", "kilometer_per_second": "km/s"}),
    currency=dict(standard_unit="Naira", standard_symbol="N", available_converts=["naira", "rand", "rand",
                                                                                  "dollars"],
                  available_units=["N", "$", "Y", "R"],
                  converts_and_units={"naira": "N", "dollars": "$", "Yuan": "Y", "rand": "R"}),
    temperature=dict(standard_unit="Kelvin", standard_symbol="K", available_converts=["Kelvin",
                                                                                      "Celsius",
                                                                                      "Farheint"],
                     available_units=["K", "C", "F"],
                     converts_and_units={"Kelvin": "K", "Celsius": "C", "Farheint": "F"})),
    files=dict(file_type=["text", "audio", "image"], conversion=dict(
        text=["csv, xlsx, txt, docx, word, pdf, epub"], audio=["mp3", "wav"], image=["jpg", "png", "jpeg"])))


# @Todo: Save the master data into dbm
"""
The code below is not working yet.

"""

###################################################

# with dbm.open("pyconvert",  "c") as db:
#     for key, value in __all__.items():
#         db[(key)] = bytes(value)

###################################################


class Validator:
    def __init__(self, name):
        self.name = name

    def is_type_valid(self):
        if not isinstance(self, str):
            raise TypeError("The name {0} is not of type str. All unit entered must be strings".format(self))
        else:
            return True

    def is_name_valid(value, self="measurement"):
        if value in __all__[self].keys():
            return True
        elif value not in __all__[self]:
            for key, values in __all__[self].items():
                    # @Todo: Try to standardize this part
                    """
                    The code below is wrong.
                    Its for testing purposes only.
                    """
                    if value in values["available_units"]:
                        return False
                    else:
                        return True
        else:
            raise TypeError("The unit {0} does not exist.".format(value))




test = Validator
test.is_name_valid("m")




#folaraz11@gmail.com
