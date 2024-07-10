#Password Generator

#import the string and random modules
import string
import random

#input from user
length=int(input("Enter password length:"))
print("Welcome to password generator")

#getting password length
print("choose character set for password from these: 1.digits  2.letters 3.special symbols 4.exit")
characterList =""

#getting character set for password
while(True):
    choice=int(input("pick a number:"))
    if(choice == 1):
        characterList += string.ascii_letters

    elif(choice == 2):
        characterList += string.digits
    
    elif(choice == 3):
        characterList += string.punctuation

    elif(choice == 4):
        break
    else:
        print("please pick a valid option:")

password = []

for i in range(length):

    #picking a random character from list
    randomchar = random.choice(characterList)

    #appending a random charter to password
    password.append(randomchar)

#printing a password as a character
print("The Random Paswword is "+"".join(password))

