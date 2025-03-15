import secrets
from random import randint
import string

def inputt():
    user=(input("Enter your preferences : ")).lower()
    user_input(user)

def user_input(user):
    match user:
        case 'strong':
            password_length(32)
        case 'medium':
            password_length(28)
        case 'basic':
            password_length(16)
        case _:
            print("invalid input")
            inputt()


def password_length(length):
    password_generator(randint(8,length))

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    print(f"PASSWORD : {password}")

print('''Hey!
  Choose your password strength
    1.strong
    2.medium
    3.basic \n''')
inputt()