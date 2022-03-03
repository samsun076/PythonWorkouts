import random

def guessing_game():
    answer = random.randint(0,100)
    #print(answer)
    
    while True:
        user_guess = int(input("Guess a Number: "))
        if user_guess == answer:
            print("Success, you correctly selected the random number ", answer)
            break
        elif user_guess < answer:
            print("TOO LOW, Please try again")
        else:
            print("too HIGH, try again")
            

guessing_game()

