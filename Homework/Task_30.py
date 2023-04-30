# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

arifmetic_progression_list = []
first_el = int(input('Введите первый элемент арифметической прогрессии: '))
arifmetic_progression_list.append(first_el)
diff_el = int(input('Введите разность между элементами арифметиечской прогрессии(d): '))
el_amount = int(input('Введите количество элементов в прогрессии: '))

for i in range(2, el_amount + 1):
    temp_el = first_el + (i - 1) * diff_el
    arifmetic_progression_list.append(temp_el)

print(arifmetic_progression_list)
