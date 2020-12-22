class Car:
    def __init__(self, name, kind, order):
        self.name = name
        self.kind= kind
        self.order = order
    def stoped(self):
        return f'{self.name}{self.kind} stoped'
    def starter(self):
        return f'{self.name}{self.kind} started'