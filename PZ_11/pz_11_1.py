"""
1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Исходные данные:
Количество элементов:
Индекс первого минимального элемента:
Умножаем все элементы на минимальный элемент:
"""
file1 = open('file1.txt', 'w')
file1.write('-9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9')
file1.close()

with open('file1.txt', 'r') as file1:
   source = file1.readline()

sourceList = source.split()
listNum = []

for i in range(len(sourceList)):
   t = int(sourceList[i])
   listNum.append(t)

sourceMin = min(listNum)
listMinNum = []

for i in range(len(listNum)):
   num = listNum[i] * sourceMin
   listMinNum.append(str(num))

result_str = ", ".join(listMinNum)


print(f'Исходные данные: {source}\n'
     f'Кол-во элементов: {len(sourceList)}\n'
     f'Индекс первого минимального элемента: {listNum.index(sourceMin)}\n'
     f'Умножаем все элементы на минимальный элемент: {result_str}')