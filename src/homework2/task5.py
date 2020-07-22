"""Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.
"""


def fibonacci(n):
    """Поиск числа фибоначчи.

    :param n: Номер числа Фибоначчи.
    :return: Число. n-ое число Фибоначчи
    """
    if n < 3:
        return 1
    f1, f2 = 1, 1
    i = 2
    while i < n:
        f1, f2 = f2, f1 + f2
        i += 1

    return f2  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 0
    print(fibonacci(n))
