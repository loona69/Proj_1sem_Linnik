"""Создайте базовый класс "Форма" со свойствами "цвет" и "тип". От этого класса
унаследуйте класс "Круг" и добавьте в него свойство "радиус". Определите методы
вычисления площади и периметра."""

class Form:
    def __init__(self, color, type):
        self.color = color
        self.type = type

    def get_form(self):
        return self.color, self.type
class Circle(Form):
    def __init__(self, color, type, radius):
        Form.__init__(self, color, type)
        self.radius = radius


    def get_circle(self):
        return self.type, self.color, self.radius

    def ploshad(self):
        self.res_plosh = 3.14 * (self.radius ** 2)
        print('Площадь кругa: ')
        return self.res_plosh
    def perim(self):
        self.res_per = 2 * 3.14 * self.radius
        print('Периметр круга: ')
        return self.res_per

OneForm = Form('Cиний', 'Квадрат')
print(OneForm.get_form())
OneCirle = Circle('Cиний', 'Круг', 23)
print(OneCirle.get_circle())
print(OneCirle.ploshad())
print(OneCirle.perim())