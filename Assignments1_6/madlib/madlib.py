def mad_libs():
    
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb ending in -ing: ")
    emotion = input("Enter an emotion: ")

    # Creates the story using f-strings
    mad_lib = (
        f"One day, {name} went to {place}. It was a very {adjective} day.\n"
        f"They saw a {noun} that was {verb} nearby, which made them feel very {emotion}.\n"
        f"{name} thought it was the best day ever at {place}!"
    )

    
    print("\nHere's your Mad Lib story:\n")
    print(mad_lib)


def main():
    mad_libs()


if __name__ == '__main__':
    main()
