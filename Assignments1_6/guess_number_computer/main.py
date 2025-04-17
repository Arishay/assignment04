import random 

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess:int = int(input("Guess a number betwween 1 and 10: "))
        if guess < random_number:
            print("Oops!your guess is too low.Guess again ")
        elif guess > random_number:
            print("Oops! Your guess is too high")

    print(f'Yay, Congrats. You guessed the correct number:  {random_number}')        


guess(10)        