from fruit import Fruit

fruit = Fruit("apple", 10, 1)

another_fruit = Fruit("orange", 12, 1.1)

hybrid_fruit = fruit + another_fruit

print(hybrid_fruit.name)
print(hybrid_fruit.__dict__)

hybrid_fruit.introduce_fruit()