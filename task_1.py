from pprint import pprint

def dict_convert(number: int) -> dict:
    return {'bin': bin(number), 'dec': number, 'hex': hex(number), 'oct': oct(number)}

list_dict = [dict_convert(i) for i in range(16)]

pprint(list_dict)
