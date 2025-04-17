PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():

    User_Age = int(input("How old are you? "))

    if User_Age >= PETURKSBOUIPO_AGE:
        print("You can Vote in Peturksbouipo.")

    else: 
        print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")


    if User_Age >= STANLAU_AGE:
        print("You can Vote in Stanlau.")

    else: 
        print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")

    if User_Age >= MAYENGUA_AGE:
        print("You can Vote in Mayengua.")

    else: 
        print("You cannot vote in Mayangua where the voting age is " + str(MAYENGUA_AGE) + ".")
    


if __name__ == '__main__':
    main()    