from move import Move
import random


class FruitSalad(Move):
    fruit_type = "salad"

    def __init__(self, fruit1, fruit2, fruit3, fruit_id=99, fall_speed=1):
        super().__init__(random.randint(0, 100), 0)
        self.fruit_id = fruit_id
        self.fruit1 = fruit1
        self.fruit2 = fruit2
        self.fruit3 = fruit3
        self.fruit_list = [self.fruit1, self.fruit2, self.fruit3]
        self.points = self.fruit1.points + self.fruit2.points + self.fruit3.points
        self.fall_speed = fall_speed

    def activate_bonus(self):
        self.fruit1.activate_bonus()
        self.fruit2.activate_bonus()
        self.fruit3.activate_bonus()

    def introduce_fruit(self):
        print(
            f"I am a {self.fruit1.name}, {self.fruit2.name}, and {self.fruit3.name} fruit {self.fruit_type}! Enjoy {self.points} points!"
        )

    def fall(self):
        super().move(0, self.fall_speed)
        print(f"Falling at {self.fall_speed}")
