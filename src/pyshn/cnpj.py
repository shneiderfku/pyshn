#########################################################################################
# Entry Point
#########################################################################################

def cnpj(value:any):
    if not (isinstance(value, int) or isinstance(value, str)):
        raise _invalid_type(value)
    return __cnpj(_parse(value))

#########################################################################################
# Helpers
#########################################################################################

def _parse(value:any) -> str:
    if isinstance(value, int):
        return _parse_from_number(value)
    else:
        return _parse_from_string(value)

def _parse_from_string(value:str) -> str:
    def fourteen():
        if value.isnumeric():
            return value
        raise _invalid_format(value)
    
    def eighteen():
        # Format:
        #
        # 01.345.789/1234-67
        #   |   |   |    |
        #   2   6   10   15
        #
        if value[2] == '.' and value[6] == '.' and value[10] == '/' and value[15] == '-':
            return ''.join([d for d in value if d.isdigit()])
        raise _invalid_format(value)

    try:
        return int({ 14: fourteen, 18: eighteen }[len(value)]())
    except KeyError as e:
        raise _invalid_format(value) from e

def _parse_from_number(value:int) -> str:
    if 1 < value > 99_999_999_999_999:
        raise _invalid_range(value)
    else:
        return _parse_from_string(f"{value:0>14}")

#########################################################################################
# Errors
#########################################################################################

class CnpjError(BaseException):
    pass

def _invalid_type(value:any):
    raise TypeError(f"cnpj: must be number or string, not '{type(value)}'")

def _invalid_range(value:any, begin=1, end=99_999_999_999_999):
    raise CnpjError(f"cnpj: must be between {begin} and {end}, its {value}")

def _invalid_format(value:any):
    raise CnpjError(f"cnpj: invalid format '{value}'")

#########################################################################################
# CNPJ Class
#########################################################################################

class __cnpj:
    _number:int

    def __init__(self, number:int):
        self._number = number
    
    def __repr__(self):
        return f"<cnpj {self._number:0>14}>"

    def __int__(self):
        return self._number

    def __str__(self):
        return format(self, 's')

    def __format__(self, format_spec):
        n = f"{self._number:0>14}"
        if format_spec == '' or format_spec == 's':
            return f"{n[0:2]}.{n[2:5]}.{n[5:8]}/{n[8:12]}-{n[12:]}"
        if format_spec == 'n':
            return n
        raise CnpjError(f"cnpj: format not supported '{format_spec}'.")
