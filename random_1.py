import random

while True:
    try:
        n = int(input("Level: "))
        if n <= 0:
            continue
        answear = random.randint(1,n)

        while True:
            guess = int(input("Guess: "))
            if guess == answear:
                print("Just Right!")
                break
            elif guess > answear:
                print("Too large!")
            else:
                print("Too small!")
        break
    except ValueError:
        continue
    
