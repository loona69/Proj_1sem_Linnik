#Организовать и вывести последовательность из N случайных чисел. Из исходной последовательности организовать последовательность, содержащую отрицательные числа. Найти количество элементов в полученных последовательностях.
from random import randint
psl = [(randint(-10, 10)) for i in range(10)]
psl_plus = [i for i in psl if i > 0]
psl_minus = [i for i in psl if i < 0]
klv_plus = len(psl_plus)
klv_minus = len(psl_minus)
print(f' Начальная последовательность : {psl};\n Последовательность с положительными числами : {psl_plus};\n Последовательность с отрицательными числами : {psl_minus};\n Количество положительных элементов : {klv_plus};\n Количество отрицательных элементов : {klv_minus}')