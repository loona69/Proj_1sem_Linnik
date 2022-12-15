#Дана строка, подсчитать в ней кол-во латинских прописных букв.

text = 'Linnik Viktoria Sdelala Practichesky'
print(len([1 for i in text if i.isupper() and ord(i) in range (65,91)]))
