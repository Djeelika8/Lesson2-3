#### Численный треугольник 1
# Дано натуральное число n. Напишите программу, которая печатает
# численный треугольник в соответствии с примером:
# 1
# 22
# 333
# 4444
# 55555
# ...

# n = int(input())
n = 8
for i in range(1, n + 1):  # Здесь количество строк n
    for j in range(i):  # Здесь элементы, то что в строке
        print(i, end='')
    print()                         # Здесь продвинули экранный курсор на следующую строку

### Численный треугольник 3
# Дано натуральное число n. Напишите программу, которая печатает численный треугольник
# с высотой равной n, в соответствии с примером:
#
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# ...

# n = int(input())
n = 8

total = 0  # счетчик
for i in range(1, n + 1):  # Здесь количество строк n.
    for j in range(1, i + 1):  # Здесь элементы, то что в строке
        total += 1
        print(total, end=' ')
    print()                         # Здесь продвинули экранный курсор на следующую строку

###  Численный треугольник 4
# Дано натуральное число n. Напишите программу, которая печатает численный треугольник
# с высотой равной n, в соответствии с примером:
#
# 1
# 121
# 12321
# 1234321
# 123454321
# ...


# n = int(input())
n = 5
for i in range(1, n + 1):  # Здесь количество строк n.
    for j in range(1, i * 2 + 1):  # Здесь элементы, то что в строке по порядку
        if j <= i:
            print(j, end='')
    for d in range(i * 2, 0, -1):  # Здесь элементы, то что в строке в обратном порядке
        if d >= i * 2 and i - 1 != 0:
            print(i - 1, end='')
            i = i - 1  # i присваеваем меньше на 1, так как печатаем в обратном порядке
    print()                       # Здесь продвинули экранный курсор на следующую строку
# -----------------------------
#### ПО ДРУГОМУ ......___________
# https://www.youtube.com/watch?v=7-z37EGoW1Y
#
# 1
# 121
# 12321
# 1234321
# 123454321


def paramid():
    odd = 1
    for i in range(1, 6):
        k = 0
        for j in range(1, odd + 1):
            if j <= i:
                k = k + 1
            else:
                k = k - 1
            print(k, end='')
        print()
        odd += 2  # здесь мы увеличиваем следующую строку на 2


paramid()

#### -- Сдвигаем Пирамиду ----------------
#
#             1
#         121
#     12321
# 1234321
#
#                         1
#                 121
#         12321
# 1234321
#

def paramid():
    odd = 1
    space = 3  # для сдвига цифр, для отступа
    for i in range(1, 5):
        k = 0
        for j in range(1, space + 1):
            print('      ', end='')  # сдвигаем пробелами
        for j in range(1, odd + 1):
            if j <= i:
                k = k + 1
            else:
                k = k - 1
            print(k, end='')
        print()
        odd = odd + 2  # здесь мы увеличиваем следующую строку на 2
        space = space - 1  # здесь мы уменьшаем отступ


paramid()
