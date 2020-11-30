Speed_1 =int(input("Скорость первого автомобиря"))
Speed_2 =int(input("Скорость второго автомобиля"))
All =int(input("Расстояние"))
Speed_Sum = Speed_1+Speed_2
Time = All/Speed_Sum
print("Автомобили встретятся через", int(Time), "час(а)")