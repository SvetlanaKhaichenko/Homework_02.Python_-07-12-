"""
3) Вводим с клавиатуры целое число - это зарплата.
Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых

"""

zp = int(input('Введите зарплату, которую необходимо рассчитать: '))
count = 0

bill25 = 25
bill10 = 10
bill3 = 3
bill1 = 1
b25 = 0
b10 = 0
b3 = 0
b1 = 0
bil10 = 0
bil3 = 0
bil1 = 0

while zp > 50:
    zp = zp - bill25
    count += 1
b25_1 = count
if zp >= bill25:
    count_res = count
    a = zp//bill25
    res = zp % bill25
    count = count + a
    b25 = b25_1 + a
    if res >= bill10:
        a = res//bill10
        res = res % bill10
        count = count + a
        b10 = a
    if res >= bill3:
        a = res//bill3
        res = res % bill3
        count = count + a
        b3 = a
    if res >= bill1:
        a = res
        count = count + a
        res = 0
        b1 = a
    if zp >= bill10:
        a = zp//bill10
        zp = zp % bill10
        count_res = count_res + a
        bil10 = a
        if zp >= bill3:
            a = zp//bill3
            count_res = count_res + a
            zp = zp % bill3
            bil3 = a
        if zp >= bill1:
            a = zp
            count_res = count_res + a
            zp = 0
            bil1 = a
    if count_res > count:
        print(
            f"Минимальное количество купюр = {count}, 25 рублевые = {b25} , 10 рублевые = {b10}, 3х рублевые = {b3}, 1 рублевые = {b1}")
    else:
        print(
            f"Минимальное количество купюр = {count_res}, 25 рублевые = {b25_1}, 10 рублевые = {bil10}, 3х рублевые = {bil3}, 1 рублевые = {bil1}")
if zp >= bill10:
    a = zp//bill10
    count = count + a
    zp = zp % bill10
    b10 = a
    if zp >= bill3:
        a = zp//bill3
        count = count + a
        zp = zp % bill3
        b3 = a
    if zp >= bill1:
        a = zp
        count = count + zp
        zp = 0
        b1 = a
    print(
        f'Минимальное количество купюр = {count}, 25 рублевые = {b25_1}, 10 рублевые = {b10}, 3х рублевые = {b3}, 1 рублевые = {b1}')
if zp >= bill3:
    a = zp//bill3
    count = count + a
    zp = zp % bill3
    b3 = a
    if zp >= bill1:
        a = zp
        count = count + zp
        zp = 0
        b1 = a
    print(
        f'Минимальное количество купюр = {count}, 25 рублевые = {b25_1}, 3х рублевые= {b3}, 1 рублевые = {b1}')
if zp >= bill1:
    a = zp
    count = count + a
    b1 = a
    print(
        f'Минимальное количество купюр = {count}, 25 рублевые = {b25_1}, 1 рублевые = {b1}')
