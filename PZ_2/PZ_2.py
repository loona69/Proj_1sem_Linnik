#Разработать программу где дается 1 любое 3значное число и вывести 1 цифру данного числа т.е. сотни используя только одну операцию деления нацело.

import random #импортируем модуль рандом
chislo1=random.randrange(100,1000) #используем модуль для получения рандомного числа от 100 до 1000
print('Данное число: ', chislo1)
chislo2=int(chislo1/100) #получение сотней
print('Сотни: ', chislo2)
