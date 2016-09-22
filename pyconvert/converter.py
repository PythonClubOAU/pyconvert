from pyconvert import validator, errors, relationships


class Converter:
    """
    Main converter class.
    Would take care of all conversions.
    All types.
    """

    def __init__(self, type="measurement"):
        self.type = type

    def convert(name, convert_from, convert_to, self=""):
        """
        self == value to convert
        name == type of conversion
        convert_from ==  where from
        convert_to == where to
        """
        if not validator.Checker.conversion_is_valid(name, convert_from=convert_from, convert_to=convert_to):
            raise errors.InvalidConversionError("The conversion is invalid.")
        else:
            relationships.Length.metres()

    def QuickConvert(self, convert_from, convert_to, type="measurement"):
        """
        This would take care of quickly making quick simple conversions.
        It should be called when the conversion varibles need to be passed straight through a class.
        """

        converted = Converter.convert(self, convert_from, convert_to)
        if converted:
            return converted
        else:
            return False

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
            if validator.Checker.conversion_is_valid(name, parameter, convert_to, convert_from):
                pass

    class FileConverter:
        """
        Base file conversion class.

        """

        def __init__(self, type="file"):
            self.type = type

        def TextConverter(self):
            pass


# Converter.convert(name="length",convert_from="metres",convert_to="centimetre")



print(dir(validator.Getter))


