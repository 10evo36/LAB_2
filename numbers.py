#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    # Ввести 4 числа
    Number_one = float(input("Введите первое число"))
    Number_two = float(input("Введите второе число"))
    Number_three = float(input("Введите третье число"))
    Number_four = float(input("Введите четвертое число"))
    # Посчитать сумму первых двух чисел и вторых двух, затем разделить сумму первых чисел на сумму вторых
    Sum_1 = Number_one + Number_two
    Sum_2 = Number_three + Number_four
    Div = Sum_1 / Sum_2
    # Вывести результат с двумя числами после запятой
    print("% .2f" % Div)
