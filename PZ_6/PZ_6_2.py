#Дан список А размера N. Сформировать 2 новых списка В и С: в список с В записать все положительные элементы список А, в список С - все отрицательные(сохраняя исходный порядок следования элементов). Вывести вначале размер и содержимое списка В, а затем - размер и содержимое списка С.

import random


def program():
   try:
       lst = [random.randint(-10, 10) for el in range(int(input("Введите размер N: ")))]  # Заполняем список 10 числами
       print(f'Список А: {lst}')  # Выводим созданный список на экран
       B = [x for x in lst if x > 0]  # Определяем положительные числа списка
       print(f'Размер списка В: {len(B)}')  # Вывод размера списка В
       print(f'Содержимое списка В: {B}')  # Вывод содержимого В
       C = [x for x in lst if x < 0]  # Определяем отрицательные числа списка
       print(f'Размер списка C: {len(C)}')  # Вывод размера списка С
       print(f'Содержимое списка С: {C}')  # Вывод содержимого С
   except ValueError:
       print("Ошибка ввода")  # Оповещание об ошибке
       program()  # Повторный вызов функции из-за ошибки


program()
