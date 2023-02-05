def str_to_lower(text_lst): # Создаём генератор
    for i in text_lst:
        if i.isdecimal():
            yield i


text = (input('Введите текст с цифрами или числами - '))
print(''.join(str_to_lower(text)))