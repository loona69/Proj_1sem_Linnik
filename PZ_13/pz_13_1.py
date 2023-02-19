from random import randint

len_m = int(input('Введите размер матрицы: '))  # ввод размера матрицы
matrix = [[randint(-100, 100) for i in range(len_m)] for j in range(len_m)]  # создание матрицы
print("Изначальная матрица: ")
for i in matrix:  # вывод матрицы
   print(*i, sep='\t' * 2)
print("\n")
print("Результат:")
for col in list(zip(*matrix))[0::2]:
   print(sum(col))