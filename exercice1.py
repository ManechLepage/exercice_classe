class StringFoo:
    def __init__(self):
        self.message = ""

    def set_string(self, message):
        self.message = message

    def print_string(self):
        print(self.message.upper())


stringFoo = StringFoo()
stringFoo.set_string("moche")
stringFoo.print_string()

