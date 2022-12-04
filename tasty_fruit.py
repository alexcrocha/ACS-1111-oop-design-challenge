from fruit import Fruit


class TastyFruit(Fruit):
    def __init__(self, name, points, fall_speed, bonus, mood):
        super(name, points, fall_speed)
        self.bonus = bonus
        self.mood = mood
    
    def activate_bonus(self):
        print('BONUS ACTIVATED')

    def boost_mood(self):
        print('BOOST MOOD')
