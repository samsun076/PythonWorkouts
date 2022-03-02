import random

def guessing_game():
    user_guess = int(input("guess a number: "))
    attempt = 0
    number = random.randint(0, 101)
    print(type(number))
    print(type(user_guess))
    print(number, " your number is ", user_guess)
    while user_guess != number:
        if user_guess < number:
            number = int(input("your number is too low, Try again: "))
            print(number)
        elif user_guess > number:
            number = int(input("your number is too high, Try again: "))
            print(number)
guessing_game()
