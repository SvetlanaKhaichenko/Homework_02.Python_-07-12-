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

if zp >= bill25:
    a = zp//bill25
    zp = zp % bill25
    count = a
    print(a, '= 25 руб')
if zp >= bill10:
    a = zp//bill10
    zp = zp % bill10
    count = count + a
    print(a, '= 10 руб')
if zp >= bill3:
    a = zp//bill3
    zp = zp % bill3
    count = count + a
    print(a, '= 3 руб')
if zp > 0:
    a = zp
    count = count + a
    print(a, '= 1 руб')



