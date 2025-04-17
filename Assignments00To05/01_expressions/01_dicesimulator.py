import random

numSides = 6

def rollDice():
  die1:int = random.randint(1,numSides)
  die2:int = random.randint(1,numSides)
  total:int = die1+die2
  print("The total of two dice is :", total)
  


def main():
  
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    rollDice()
    rollDice()
    rollDice()
    print("die1 in main() is: " + str(die1))

if __name__ == '__main__':
  main()