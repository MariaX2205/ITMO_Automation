class Car():

    def __init__(self, type, year, color, e):
        self.type = type
        self.year = year
        self.color = color
        self.e = e

    def start(self):
        if self.e:
            print('Автомобиль заведен')
        else:
            print('Автомобиль заглушен')

    def type(self):
        return self.type

    def year(self):
        return self.year

    def color(self):
        return self.color


c = Car('Ford', '2020', 'white', '1')
c.start()
print('Автомобиль: ', c.type, c.year, c.color)
