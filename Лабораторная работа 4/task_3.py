def delete(list_, index=None):

    """Функция удаления элемента из списка по индексу"""

    if index != None:
        list_left = list_[:index]
        list_right = list_[index+1:]
        list_new = list_left + list_right
    else:
        list_new = list_[:-1]

    return list_new

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
