def add3copies(my_list,data):
    for i in range(3):
        my_list.append(data)

def main():
    msg:str = str(input("Enter a message to copy: "))
    my_list = []
    print("List before,",my_list)
    add3copies(my_list, msg)
    print("List after:", my_list)

if __name__ == '__main__':
    main()            