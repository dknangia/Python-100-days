import random

#Random payer program
friends = ["Ron", "Michale", "Charlotte", "Sam", "Shaun"]

random_payer = random.randint(0, len(friends)-1)

print(friends[random_payer])
