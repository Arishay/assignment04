def main():
    num1:int = int(input("Enter first number: ")) 
    num2:int = int(input("Enter second number: "))

    average:int = (num1 + num2)/2

    print("The average of {} and {} is {}".format(num1,num2,average)) 



if __name__ == '__main__':
    main()    