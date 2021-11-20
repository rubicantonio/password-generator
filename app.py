
import string
import random
def generatePassword(j):

    var1 = string.ascii_letters
    i = 0
    password = []
    while i < j:
            var2 = random.choice(string.ascii_letters)
            password.append(var2)
            i += 1


    print("".join(password))
#generatePassword()
