class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Starting drawing {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You take {self.title}: Starting drawing with a Pen...'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You take {self.title}: Starting drawing with a Pencil...'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You take {self.title}: Starting drawing with a Marker... '


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Marker')
print(pen.draw())
print(pencil.draw())
print(handle.draw())