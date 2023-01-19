"""
2. Из предложенного текстового файла (text18-14.txt) вывести на экран его содержимое,
количество пробельных символов. Сформировать новый файл, в который поместить текст
в стихотворной форме предварительно заменив символы третей строки их числовыми
кодами.
"""
t = 0
d = 0
for i in open('text18-14.txt', encoding='UTF-8'):
   print(i, end='')
   t += 1
   for j in i:
       if j == ' ':
           d += 1
print(end='\n')
print('Количество пробельных символов: ', d, end='\n')

f1 = open('text18-14.txt', 'r', encoding='UTF-8')
l = f1.readlines()

ascii_values = []
for character in l[2]:
   ascii_values.append(ord(character))
l[2] = ''.join(str(ascii_values)) + "\n"

f1.close()
f2 = open('text2.txt', 'w', encoding='UTF-8')
f2.writelines(l)
f2.close()

for i in open('text2.txt', encoding='UTF-8'):
   print(i, end='')
   t += 1
   for j in i:
       if j == ' ':
           d += 1
print(end='\n')







