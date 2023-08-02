# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

print('Input the first number in your list:')
first_elem = int(input())
print('Input by what number your next elements will change: ')
change_by_num = int(input())
print('Input the number of elements in your list: ')
num_of_elems = int(input())

def arithmetic_progression (first_elem, change_by_num, num_of_elems) -> str:
    for i in range(num_of_elems):
        print(first_elem + (i) * change_by_num, end = " ")

arithmetic_progression (first_elem, change_by_num, num_of_elems)