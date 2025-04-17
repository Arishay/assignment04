import random
import string

def generte_pass(length = 12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


length = int(input("Enter the length of your desired password: "))

password = generte_pass(length) 
print("Generated password: ",password)
