def get_count_char(str_):

    """Функция, которая принимает строку и возвращает словарь
        с частотой каждой буквы, присутвующей в этой строке.
        Причем символы расположены в алфовитном порядке"""

    dictionary_symbols = {} # Создание пустого словаря
    str_ = str_.lower() # Приведение строки к нижнему регистру
    chars = list(str_) # Из строки делаем список, где элементами списка являются символы строки
    chars.sort() # Сортируем список по алфовиту
    for char in chars:
        symbol_is_letter = char.isalpha()
        if symbol_is_letter == True: # условие проверки элементов массива на принадлежность к буквам
            number_symbols = chars.count(char)
            dictionary_symbols[char] = number_symbols

    return dictionary_symbols # функция возвращает словарь, у которого: ключ - символ; значение - количество символов

def get_percent_char(dictionary):

    """Функция, которая принимает словарь с буквами
        в качестве ключа и количеством букв в качестве
        значений и возвращает новый словарь, где количество
        каждого элемента заменено на процентное отношение
        ко всем символам"""

    dictionary_percent_symbols = {} # Создание пустого словаря
    values = dictionary.values() # Из словаря достаем только значения и записываем их в список
    sum_values = sum(values) # Суммируем все элементы списка
    for key in dictionary:
        dictionary_percent_symbols[key] = dictionary_symbols[key] * 100 / sum_values # процентное отношение

    return dictionary_percent_symbols # функция возвращает словарь, где количество каждого элемента заменено на процентное отношение ко всем символам

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

dictionary_symbols = get_count_char(main_str)

print(get_count_char(main_str))
print(get_percent_char(dictionary_symbols))
