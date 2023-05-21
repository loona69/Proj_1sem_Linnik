"""Создайте класс "Машина" с атрибутами "марка", "модель" и "год выпуска".
Напишите метод, который выводит информацию о машине в формате
"Марка: марка, Модель: модель, Год выпуска: год"""

class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

    def get_machin(self):
        return 'Марка:', self.mark,'Модель: ', self.model, 'Год выпуска: ', self.year

OneCar = Car('Opel', '235235', '21 года')
print(OneCar.get_machin())