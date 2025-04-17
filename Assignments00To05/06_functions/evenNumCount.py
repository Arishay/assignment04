def count_even(lst):
    
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        
        num = int(user_input)
        lst.append(num)
        user_input = input("Enter an integer or press enter to stop: ")

    
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1

    
    print("Number of even numbers:", even_count)
def main():
    numbers = []
    count_even(numbers)


if __name__ == '__main__':
    main()
