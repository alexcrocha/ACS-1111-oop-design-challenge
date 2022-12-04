class Fruit():
    is_edible = True
    list_of_fruits = [ ]
    def __init__(self, name, points, fall_speed):
        self.name = name
        self.points = points
        self.fall_speed = fall_speed
     
    def create_fruit(self):
        self.list_of_fruits.append(Colour('red', 5))

    def fall(self):
        print(f'Falling at {self.fall_speed}')
    
    def introduce_fruit(self):
        print(f'I am a {self.name} and my point value is {self.points}')

    def __add__(self, another_fruit):
        """Override the add magic method to create a new hybrid fruit object 
        and give it a merged name"""
        hybrid_fruit = f"{self.name}-{another_fruit.name}"
        hybrid_points = (self.points + another_fruit.points) / 2
        hybrid_fall_speed = (self.fall_speed + another_fruit.fall_speed) / 2
        return Fruit(hybrid_fruit, hybrid_points, hybrid_fall_speed)
