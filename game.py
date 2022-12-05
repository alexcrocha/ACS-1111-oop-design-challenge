from tree import Tree
from pig import Pig


roadhog = Pig("Roadhog")
tree = Tree()
iteration = 0

while roadhog.is_hungry:
    iteration += 1
    if iteration % 5 == 0:
        tree.create_fruit()
    direction = input("\nWASD to move your little piggy! > ")
    x = 1 if "d" in direction else -1 if "a" in direction else 0
    y = 1 if "s" in direction else -1 if "w" in direction else 0

    roadhog.move(x, y)
    for fruit in tree.fruit_list:
        fruit.fall()
        if fruit.x == roadhog.x and fruit.y == roadhog.y:
            roadhog.eat(fruit)
            tree.delete_fruit(fruit)
    if roadhog.health >= 300:
        print("Pig is full!")
        roadhog.is_hungry = False
    else:
        print(f"Health: {roadhog.health}")
        print("Pig is still hungry!")

print("Game over!")
