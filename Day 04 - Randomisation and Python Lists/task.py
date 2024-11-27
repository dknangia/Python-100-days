import random

# randomNumber = random.randint(10, 25)
# print(randomNumber)
#
# randomNumber_0_to_1 = random.random()
# print(round(randomNumber_0_to_1, 2))
#

#Random heads or tails.

random_heads_or_tails = random.randint(0,1)

if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
