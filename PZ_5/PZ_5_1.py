s = input('Введите слово: ')
w = int(input('Введите ширину(целое значение): '))
def ramka():
print(f"{'-'*w}\n|{s.center(w-2)}|\n{'-'*w}")
ramka()
