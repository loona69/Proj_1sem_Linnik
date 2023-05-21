import re  # импорт библиотеки re

f1 = open('hotline1.txt', 'r', encoding='UTF-8').read()  # открытие файла
f = re.findall(r"(8?.\(8\d{2}\)?.\d{3}-\d{2}-\d{2})", f1)  # регулярное выражени
result = list(set(f))
print('Номера телефонов: ', ', '.join(result))
print('Количество элементов:', len(result))
print('\n')
# Вторая часть задания(Изменение текста)->

oldfile = open('hotline1.txt', encoding='UTF-8')
read = oldfile.readlines()
oldfile.close()
newfile = open('reload_hotline1.txt', 'w', encoding='UTF-8')
for x in read:
    string = re.sub('«Горячая линия»', '«Горячая линия Министерства образования Ростовской области»', x)
    newfile.writelines(string)
newfile.close()
for i in open('reload_hotline1.txt', encoding='UTF-8'):
    print(i, end='')
print('\n')