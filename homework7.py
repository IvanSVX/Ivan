first = int(input('Введите число 1: '))
second = int(input('Введите число 2: '))
third = int(input('Введите число 3: '))
if first == second == third:
    print(3)
elif first == second != third or first != second == third or first == third != second:
    print(2)
else:
    print(0)
