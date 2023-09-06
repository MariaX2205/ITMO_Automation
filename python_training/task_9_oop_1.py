class Input:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


search = Input('text', 'name')
print(search.loc)

class Button:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

press = Button('text', 'locator')
print(press.text, press.loc)

class Title:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
write = Title("this is a ", "new Title")
print(write.text, write.loc)

class Link:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
click = Link('this is a ', 'new link')
print(click.text, click.loc)
