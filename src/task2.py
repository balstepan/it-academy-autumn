"""
Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.
"""


def list_practice():
    lst = [i + j for i in 'ab' for j in 'bcd']
    print(lst)
    lst1 = lst[::2]
    print(lst1)
    lst = [i + 'a' for i in '1234']
    print(lst)
    print(lst.pop(1))
    lst1 = lst + ['2a']
    print(lst)
    print(lst1)

if __name__ == '__main__':
    list_practice()
