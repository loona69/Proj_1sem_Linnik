a = int(input()) #Написать целое число

if a > 0: #если а больше 0
   a = a + 1 #то прибавляется 1
elif a < 0: #если а меньше 0
   a = a - 2 #то уменьшаем а на 2
elif a == 0: #если а равно нулю
   a = 10 #то присваиваем значению а 10
print(a) #на экран выводится а