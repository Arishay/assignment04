SENTENCE_START: str = "Coding is fun. I learned to program and used Python to make my "

def main():

    adj:str = str(input("\nPlease type an adjective and press enter."))
    noun:str = str(input("\nPlease type a noun and press enter."))
    verb:str = str(input("\nPlease type a verb and press enter."))

    print(SENTENCE_START + adj + " " + noun + " " + verb + "!")


if __name__ == '__main__':
    main()    