# !/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    # Известна скорость превого автомобиля, второго и расстояние.
    # Найти время, через которое автомобили встретятся
    speed1 = int(input("Скорость первого автомобиря"))
    speed2 = int(input("Скорость второго автомобиля"))
    all = int(input("Расстояние"))

    # Общая скорость автомобилей.
    speed_sum = speed1 + speed2

    # Время через которое автомобили встретятся.
    time = (all / speed_sum)
    print("Автомобили встретятся через", int(time), "час(а)")
    
