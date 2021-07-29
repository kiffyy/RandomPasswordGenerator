# A PROGRAM TO RANDOMLY GENERATE STRONG PASSWORDS FOR YOU
import random

print("WELCOME TO YOUR PASSWORD GENERATOR")

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*.,~\()'

number = input("Amount of passwords to generate: ")
number = int(number)

length = input("Input your password length: ")
length = int(length)

print('\nHere are your passwords')

for pwd in range(number):
    passwords = ' '
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
