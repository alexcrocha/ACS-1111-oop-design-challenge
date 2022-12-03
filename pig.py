from move import Move


class Pig(Move):
    mood: 25
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health

    def eat(self, fruit):
        self.health += fruit.points
        fruit.activate_bonus()
        fruit.boost_mood()

    def move(self, direction):
        print(f'Moving to the {direction}')

    pass