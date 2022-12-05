from tasty_fruit import TastyFruit


class RottenFruit(TastyFruit):
    fruit_type = "rotten"

    def __init__(self, name, fruit_id=99, fall_speed=4):
        super().__init__(name, fruit_id, fall_speed)
        self.points = len(self.name) * -1

    def inflict_illness(self):
        print("Make PIG ill!")

    def activate_bonus(self):
        return self.inflict_illness()
