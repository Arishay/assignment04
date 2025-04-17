def add_many_numbers(numbers)->int:
    num:int = 0

    for i in numbers:
        num+=i
    return num

def main():
    numbers:list[int] = [1,2,3,4,5,6]
    sumOfNumbers:int = add_many_numbers(numbers)
    print(sumOfNumbers)

if __name__ == '__main__':
    main()        