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

    def add_type(self, type_new):
        self.type=type_new

    def add_year(self, year_new):
        self.year=year_new

    def add_color(self, color_new):
        self.color=color_new


