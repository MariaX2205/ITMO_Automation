class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def square(self):
        square = self.width * self.length
        return square

    def perimeter(self):
        perimeter = self.length * 2 + self.width * 2
        return perimeter


obj1 = Rectangle(10, 20)
print(obj1.square(), obj1.perimeter())
obj2 = Rectangle(25, 45)
print(obj2.square(), obj2.perimeter())
obj3 = Rectangle(55, 55)
print(obj3.square(), obj3.perimeter())


class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        addition = self.a + self.b
        return addition

    def substraction(self):
        substraction = self.a - self.b
        return substraction

    def multipilication(self):
        multiplication = self.a * self.b
        return multiplication

    def division(self):
        division = self.a / self.b
        return division


x = Math(10, 5)
print(x.addition(), x.substraction(), x.multipilication(), x.division())


class Buttons_for_demoqa():
    type = 'button'

    def __init__(self, text, loc=""):
        self.text = text
        self.loc = loc

    def click(self) -> object:
        assert isinstance(self.text, object)
        print("Click the button - {}".format(self.text))


text_box = Buttons_for_demoqa('TEXT BOX', "")
check_box = Buttons_for_demoqa("CHECK BOX", "")
radio_button = Buttons_for_demoqa("RADIO BUTTON", "")
web_tables = Buttons_for_demoqa("WEB TABLES", "")
buttons = Buttons_for_demoqa("BUTTONS", "")
links = Buttons_for_demoqa("LINKS", "")
broken_links = Buttons_for_demoqa("BROKEN LINKS", "")
upload_download = Buttons_for_demoqa("UPLOAD / DOWNLOAD", "")
dynamic_properties = Buttons_for_demoqa("DYNAMIC PROPERTIES", "")

print(text_box.text, check_box.text, radio_button.text, web_tables.text, buttons.text, links.text, broken_links.text,
      upload_download.text, dynamic_properties.text, sep="\n")

text_box.click()
check_box.click()
radio_button.click()
web_tables.click()
buttons.click()
links.click()
broken_links.click()
upload_download.click()
dynamic_properties.click()

