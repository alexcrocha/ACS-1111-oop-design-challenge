class Fruit():
    list_of_fruits = [ ]
    def __init__(self, name, points, fall_speed):
        self.name = name
        self.points = points
        self.fall_speed = fall_speed
     
    def create_fruit(self):
        self.list_of_fruits.append(Colour('red', 5))

    def fall(self):
        print(f'Falling at {fall_speed}')
