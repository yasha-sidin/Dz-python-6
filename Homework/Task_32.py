# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]
import random

main_list = []
result_list = []
for i in range(20):
    main_list.append(random.randint(-10, 50))
print(main_list)

start_check = int(input('Введите начало диапозона чисел поиска: '))
end_check = int(input('Введите конец диапозона чисел поиска: '))

for i in main_list:
    if (i >= start_check and i <= end_check):
        result_list.append(main_list.index(i))
print(result_list)