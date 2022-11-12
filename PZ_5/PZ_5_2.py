a,b,c = map(int,input('Введите три числа в строчку через пробел:').split())
print('A1 =', a,'B1 =', b,'C1 =', c )
a2,b2,c2 = map(int,input('Введите три числа в строчку через пробел:').split())
print('A2 =', a2,'B2 =', b2,'C2 =', c2 )
def ShiftLeft(a,b,c,a2,b2,c2):
 a = a+b
 b = a-b
 a = a-b
 c = c+b
 b = c-b
 c = c-b
 a2 = a2+b2
 b2 = a2 - b2
 a2 = a2 - b2
 c2 = c2 + b2
 b2 = c2 - b2
 c2 = c2 - b2
 return(a,b,c,a2,b2,c2)
z,x,c,z1, z2, z3 = ShiftLeft(a,b,c,a2,b2,c2)
print(f'Готовый циклический сдвиг влево: \nA1 ={z} B1 = {x} C1 ={c}\nA2 = {z1} B2 = {z2} C2 = {z3}')