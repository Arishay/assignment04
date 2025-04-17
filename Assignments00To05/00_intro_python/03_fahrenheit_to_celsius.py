print("\n👋--__-- Welcome to Temperature Converter \n")

def main():
   
    

 temp_in_faren = int(input("\nEnter temperature in Fahrenheit: "))
 faren_celsius = int(temp_in_faren - 32) * 5.0/9.0
 print("\nTemperature in farenheit {}F is equal to {}C ".format(temp_in_faren,faren_celsius))


 print("\nThankyou❕ for using my program\n")
 print("Made by Arisha Ghaffar😊\n")

if __name__ == '__main__':
    main()