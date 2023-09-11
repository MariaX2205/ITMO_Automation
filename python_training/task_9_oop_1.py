from python_training.task_9_checks import Checks


class Input(Checks):

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
        super().__init__(self.loc)


search = Input('text', 'name')
print(search.loc, search.text)


class Button(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
        super().__init__(self.loc)


press = Button('text', 'locator')
print(press.text, press.loc)


class Title(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
        super().__init__(self.loc)


write = Title("this is a ", "new Title")
print(write.text, write.loc)


class Link(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
        super().__init__(self.loc)


click = Link('this is a ', 'new link')
print(click.text, click.loc)
