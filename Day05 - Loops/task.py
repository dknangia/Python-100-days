
for counter in range(1,101):
    if counter % 3 == 0 and counter % 5 == 0:
        print("FizzBuzz")
        continue
    if counter % 3 == 0:
        print("Fizz")
        continue
    if counter % 5 == 0:
        print("Buzz")
        continue
    print(counter)