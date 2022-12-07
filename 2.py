"""
2) Вводим с клавиатуры целое число X
Далее вводим Х целых чисел.
Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.

"""

x = int(input("Введите целое число: "))
print(f"Введите {x} целых чисел")

if x == 1:
    max1 = int(input('число ='))
    max2 = max1
elif x == 2:
    for i in range(1):
        max1 = int(input('число = '))
        max2 = int(input('число = '))
elif x > 2:
    max1 = int(input('число = '))
    max2 = int(input('число = '))
    if max1 < max2:
        a = max2
        max1 = max2
        max1 = a
    x = x-2
    while x != 0:
        a = int(input('число = '))
        if a > max1:
            c = max1
            max1 = a
            if c > max2:
                max2 = c
        elif a > max2:
            max2 = a
        x -= 1

print(f'Максимальные введенные числа равны: {max1}, {max2}')
