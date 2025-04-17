C: int = 299792458  # Speed of light in m/s

def main():
    massInKg = float(input("Enter mass in kg: ")) 
    energy: float = massInKg * C ** 2

    print("\ne = m*c^2\n")
    print("m = {} Kg\n".format(massInKg))
    print("C = {} m/s\n".format(C))
    print("{} joules of energy!\n".format(energy))

if __name__ == '__main__':
    main()
