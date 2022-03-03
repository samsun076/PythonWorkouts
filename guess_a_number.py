import random

def guessing_game():
    answer = random.randint(0,100)
    print(answer)
    
    while True:
        user_guess = int(input("Guess a Number: "))
        if user_guess == answer:
            print("Success, you correctly selected the random number ", answer)
            break
        elif user_guess < answer:
            print("your guess of ", user_guess, " is too low, Please try again")
        else:
            print("your guess of ", user_guess, " is too HIGH, try again")
            

guessing_game()

