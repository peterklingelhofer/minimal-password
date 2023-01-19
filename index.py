from random import randint

characters = int(input('Enter password length:'))
password = []

while len(password) < characters:
    password.append(chr(randint(33, 127)))

print(''.join(password))