import random
from list_of_fruits import list_of_fruits
from tasty_fruit import TastyFruit
from rotten_fruit import RottenFruit
from fruit_salad import FruitSalad


class Tree:
    fruit_list = [
        TastyFruit(list_of_fruits[random.randint(0, len(list_of_fruits) - 1)])
    ]

    def create_fruit(self):
        fruit_index = random.randint(0, len(list_of_fruits) - 1)
        fruit_name = list_of_fruits[fruit_index]
        rotten_fruit_name = f"rotten {fruit_name}"

        random_choice = random.random()
        if random_choice < 0.65:
            # 65% chance of being a tasty fruit
            fruit = TastyFruit(fruit_name, len(self.fruit_list))
        elif random_choice < 0.9:
            # 25% chance of being a rotten fruit
            fruit = RottenFruit(rotten_fruit_name, len(self.fruit_list))
        else:
            # 10% chance of being a fruit salad
            # Fruit salad is composed of 3 random fruits. They can be either Tasty Fruit or Rotten Fruit
            fruit1 = (
                TastyFruit(list_of_fruits[random.randint(0, len(list_of_fruits) - 1)])
                if random.random() < 0.5
                else RottenFruit(
                    f"rotten {list_of_fruits[random.randint(0, len(list_of_fruits) - 1)]}"
                )
            )
            fruit2 = (
                TastyFruit(list_of_fruits[random.randint(0, len(list_of_fruits) - 1)])
                if random.random() < 0.5
                else RottenFruit(
                    f"rotten {list_of_fruits[random.randint(0, len(list_of_fruits) - 1)]}"
                )
            )
            fruit3 = (
                TastyFruit(list_of_fruits[random.randint(0, len(list_of_fruits) - 1)])
                if random.random() < 0.5
                else RottenFruit(
                    f"rotten {list_of_fruits[random.randint(0, len(list_of_fruits) - 1)]}"
                )
            )

            fruit = FruitSalad(fruit1, fruit2, fruit3, len(self.fruit_list))

        self.fruit_list.append(fruit)

    def delete_fruit(self, fruit):
        self.fruit_list.pop(fruit.fruit_id)
