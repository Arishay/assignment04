import math


def main():

    AB:float = float(input("\nEnter the length of side AB: \n"))
    AC:float = float(input("Enter the length of side AC: \n"))
    BC:float = math.sqrt(AB**2 + AC**2)

    print("The length of side BC(hypotenues)is:{} \n".format(str(BC)))




if __name__ == "__main__":
    main()    