from move import Move


class Pig(Move):
    mood = []
    is_hungry = True

    def __init__(self, name, health=100):
        super().__init__(50, 0)
        self.name = name
        self.health = health

    def eat(self, fruit):
        self.health += fruit.points
        fruit.activate_bonus()
        fruit.introduce_fruit()
        if self.health <= 0:
            self.is_hungry = False
            print("Pig is dead!")

    def move(self, x, y):
        super().move(x, y)
        print(f"Pig {self.name} moved to {self.x}, {self.y}")
