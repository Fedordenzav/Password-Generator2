import random

all_symbols = "15071021fzFZggGG123098"
lenght = int(input("Введите кол-во символов!"))
password = ""
for i in range(lenght):
    password += random.choice(all_symbols)

print(password)

sogl = "qwrtpsdfghjklzxcvbnm"
glas = "euioa"
numbers = "0123456789"
symbol = "@#$!?/"
password = ""
for i in range(4):
    password += random.choice(sogl)
    password += random.choice(glas)
for i in range(2):
    password += random.choice(numbers)
    password += random.choice(symbol)
print(password)
