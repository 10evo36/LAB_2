!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    # Ввести 4 числа.
    number1 = float(input("Введите первое число"))
    number2 = float(input("Введите второе число"))
    number3 = float(input("Введите третье число"))
    number4 = float(input("Введите четвертое число"))

    # Посчитать сумму первых двух чисел и вторых двух, затем разделить
    # сумму первых чисел на сумму вторых.
    sum1 = number1 + number2
    sum2 = number3 + number4
    div = sum1 / sum2

    # Вывести результат с двумя числами после запятой.
    print("% .2f" % div)
