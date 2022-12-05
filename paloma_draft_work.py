# from tasty_fruit import TastyFruit
# from rotten_fruit import RottenFruit


# class FruitSalad(TastyFruit, RottenFruit):
#     vessel = "Bowl"

#     def __init__(self, name, points, fall_speed, bonus, mood, illness, num_fruits):
#         super(name, points, fall_speed, bonus, mood, illness)

#I removed some attributes, I was just simplifying while I was working on it
#  I just put this here while I was working on it
class Fruit():
    is_edible = True
    list_of_fruits = [ ]
    def __init__(self, name, points, fall_speed):
        self.name = name
        self.points = points
        self.fall_speed = fall_speed
    # add the line below to Fruit class
        self.fruit_salad = None 



class FruitSalad():
    vessel = "Bowl"
    def __init__(self, name, points, fall_speed, num_fruits):
        self.name = name
        self.points = points
        self.fall_speed = fall_speed
        self.fruits = []
        self.num_fruits = num_fruits

    def add_fruit(self, fruit):
        fruit.fruit_salad = self
        self.fruits.append(fruit)
    
    def print_recipe(self):
        print(f"Recipe for {self.name}")
        for fruit in self.fruits:
            print(fruit.name)


todaysSalad = FruitSalad("Watermelon Salad", 50, 1, 5)
ingredient_1 = Fruit("watermelon", 5, 1)
ingredient_2 = Fruit("honeydew", 5, 1)
todaysSalad.add_fruit(ingredient_1)
todaysSalad.add_fruit(ingredient_2)

todaysSalad.print_recipe()
