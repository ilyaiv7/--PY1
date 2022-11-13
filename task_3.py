from random import randint

def get_unique_list_numbers() -> list[int]:
    list_random = []
    while len(list_random) != 15:
        number_random = randint(-10, 10)
        list_random = [number_random for element in list_random if number_random not in list_random]
    return list_random

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
