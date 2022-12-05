import random
from move import Move
from list_of_bonus import bonus_list


class TastyFruit(Move):
    fruit_type = "tasty"

    def __init__(self, name, fruit_id=99, fall_speed=2):
        super().__init__(random.randint(0, 100), 0)
        self.fruit_id = fruit_id
        self.name = name
        self.points = len(self.name)
        self.fall_speed = fall_speed
        self.bonus = random.choice(bonus_list)

    def activate_bonus(self):
        print(f"BONUS {self.bonus} ACTIVATED")

    def boost_mood(self):
        print("BOOST MOOD")

    def introduce_fruit(self):
        print(
            f"I am a {self.name} and I am a {self.fruit_type} fruit! Enjoy {self.points} points!"
        )

    def fall(self):
        super().move(0, self.fall_speed)
        print(f"{self.name} falling at {self.fall_speed} speed. {self.x}, {self.y}")
