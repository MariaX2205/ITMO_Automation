class Button:

    type:  str = 'Кнопка' # это константа для всех объектов

    def __init__(self, text, link):
        self.text = text
        self.link = link

# создаем экземпляры класса:
home = Button(' Домой', '/home')
catalogue_msk = Button('каталог', '/msk/catalogue')

# получаем доступ к атрибутам
print(home.text)

print('кнопка' + home.text + ' имеет ссылку' + home.link)

print('\n')

print(catalogue_msk.text)
print('Кнопка ' + catalogue_msk.text + ' имеет ссылку ' + catalogue_msk.link)

print(home.type)
print(catalogue_msk.type)

class ButtonTwo:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc
    def click(self):
        return "Клик по локатору - {}".format(self.loc)

# создаем экземпляры класса
home_two = ButtonTwo ('Домой', '/home', 'button#home')

#вызываем метод
print(home_two.click())