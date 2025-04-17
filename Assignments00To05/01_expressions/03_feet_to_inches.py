def main():

    inch_in_foot: float = 12

    foot = float(input("Enter number of feet : "))
    inch:float = foot * inch_in_foot
    print("{} foot is equals to {} inches".format(foot,inch))


if __name__ == '__main__':
    main()