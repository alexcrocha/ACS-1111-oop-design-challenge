from fruit import Fruit


class RottenFruit(Fruit):
    def __init__(self, name, points, fall_speed, illness, ):
        super(name, points, fall_speed)
        self.illness = illness

    def inflict_illness(self):
        print('Make PIG ill!')
    pass