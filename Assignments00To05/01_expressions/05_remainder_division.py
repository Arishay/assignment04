def main():
    dividend:int = int(input("\nEnter an integer to be divided: "))
    divisor:int = int(input("\nEnter an integer to divide by: "))
    quotient:int = dividend // divisor
    remainder:int = dividend % divisor

    print("\nThe result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

if __name__ == '__main__':
    main()    