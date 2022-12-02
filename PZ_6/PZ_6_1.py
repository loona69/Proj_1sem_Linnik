import random


def program():
   try:
       result = []
       count = []
       lst = [random.randint(1, 10) for el in range(int(input("Введите размер списка: ")))]  # Заполняем список 10 числами
       print(f'Сам массив: {lst}')  # Выводим созданный список на экран
       for i in range(1, len(lst), 2): # Проходим по нечётным индексам
           result.append(lst[i])  # Заполняем новый список полученными значениямим
       print(f'Массив с нечетными номерами в порядке возрастания номеров: {result}')
       for i in range(0, len(lst), 2):  # Проходим по чётным индексам
           count.append(lst[i]) # Заполняем новый список полученными значениямим
       count.reverse()  # Переварачиваем список
       print(f'Массив с четными номерами в порядке убывания номеров: {count}')
   except ValueError:
       print("Ошибка ввода")  # Оповещание об ошибке
       program()  # Повторный вызов функции из-за ошибки


program()
