#Дана строка-предложение на русском языке. Подсчитать в строке содержащихся в ней гласных букв.

stroka = 'Линник Виктория сделала практическую работу номер 7'
print('Количество гласных букв равно: ', len([c for c in stroka if c in 'аоуыиэяюёе']))
