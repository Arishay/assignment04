import random 

def computer_guess(x):
    low = 0
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else :
            low = high
        feedback = input(f'Is {guess} too high (H) , too Low (L) , correct (C) : '.lower())    

        if feedback == 'h' :
            high = guess - 1

        elif feedback == 'l':
            low = guess + 1           

    print(f"Yay, The computer guessed the correct number {guess}")        

computer_guess(100)
