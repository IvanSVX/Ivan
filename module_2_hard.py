
from random import randint
number = randint(3, 20)

password = []

for i in range(1, 21):
    for j in range(i + 1, 21):
        if number % (i + j) == 0:
            password.append(str(i) + str(j))

print(number, '-', ''.join(password))