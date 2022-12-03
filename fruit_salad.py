from tasty_fruit import TastyFruit
from rotten_fruit import RottenFruit


class FruitSalad(TastyFruit, RottenFruit):
    def __init__(self, name, points, fall_speed, bonus, mood, illness):
        super(name, points, fall_speed, bonus, mood, illness)
