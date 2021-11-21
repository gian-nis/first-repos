import random

a = ["GorillA", "SavannA", "ApplE", "PotatO", "ElevatoR", "PortaL", "ElastiC", "AstrologY"]

b = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

c = ["!", "$", "_", "?", "#"]

random_word = random.choice(a)

random_number = random.choice(b)
random_number2 = random.choice(b)
random_number3 = random.choice(b)
random_number4 = random.choice(b)

random_symbol = random.choice(c)
random_symbol2 = random.choice(c)

password = [random_word, random_number, random_symbol, random_number2, random_number3, random_number4, random_symbol2]

random.shuffle(password)

def listToString(password):

    str1 = ""

    for ele in password:
        str1 += ele

    return str1

print(listToString(password))

