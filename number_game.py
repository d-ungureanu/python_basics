import random

game_random_number = random.randint(1, 100)
game_start_message = "Guess a number in the range 1-100:"
game_active = True

while game_active:
    print(game_start_message)
    user_guess = int(input())
    if user_guess == game_random_number:
        print("You guessed the number")
        break
    elif user_guess < game_random_number:
        print("Too low, guess again")
    else:
        print("Too high, guess again")
