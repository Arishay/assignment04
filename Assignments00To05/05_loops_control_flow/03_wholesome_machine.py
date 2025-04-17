Affirmation:str = "I am capable of doing anything I put my mind to." 


def main():
     print("Please type the following affirmation: " + Affirmation)

     user_response = input()

     while user_response != Affirmation:
          
          print("That was not the affirmation.")

          print("Please type the following affirmation: " + Affirmation)

          user_response = input() 

     print("Thats Right!")              

if __name__ == '__main__':
     main()