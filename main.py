# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1

# some_list = [int(input('Enter numbers: ')) for _ in range(int(input('Enter list size: ')))]
# counter = 0
# digit = int(input('Введите число: '))
# for index in range(0, len(some_list) - 1):
#     counter = some_list.count(digit)
# print(counter)


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

some_list = [int(input('Enter numbers: ')) for _ in range(int(input('Enter list size: ')))]
size = len(some_list) - 1
nextDigit = 0
digit = int(input('Введите число: '))
for i in range(0, size):
    if some_list[i] + 1 >= some_list[digit]:
        nextDigit = some_list[i] + 1
        print(nextDigit)
        break

