import random

def main():

   sec_num = random.randint(1,99)

   print("I am thinking of a number between 1 and 99...")

   guess = int(input("Enter a guess: "))

   while guess != sec_num:
        if guess < sec_num:  
            print("Your guess is too low")
        else:
            print("Your guess is too high")

    

        print() 
        guess = int(input("Enter a new guess: "))          
   
   print("Congrats! The number was: " + str(sec_num))


if __name__ == '__main__':
    main()    