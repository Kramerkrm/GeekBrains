class Auto:
    # atributes
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Auto):

    def show_speed(self):
        return f'Speed of {self.name} is higher than allow for town car!!' \
            if self.speed > 60 else f'Speed of {self.name} is normal for town car'


class WorkCar(Auto):

    def show_speed(self):
        return f'Speed of {self.name} is higher than allow for work car!!' \
            if self.speed > 40 else f'{self.name}: Car speed {self.speed}'


class PoliceCar(Auto):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


class SportCar(Auto):
        ''' Sport Car '''


CHEVROLET = TownCar(30,  'White', "'Chevrolet'")
CHEVROLET.go()
print(CHEVROLET.show_speed())
CHEVROLET.turn_left()
CHEVROLET.stop()
print()

Toyota = WorkCar(70, 'Rose', "'Toyota'")
Toyota.go()
print(Toyota.show_speed())
Toyota.turn_right()
Toyota.stop()
print()

FORD = PoliceCar(60, 'Blue', "'Ford'")
FORD.go()
print(FORD.show_speed())
FORD.turn_left()
FORD.stop()
print()

BMW = SportCar(120, 'White', "'Bmw'")
BMW.go()
print(BMW.show_speed())
BMW.turn_right()
BMW.stop()

