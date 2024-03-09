import random

# user input parameters
def set_limits():
    while True:
            lower_limit = int(input("Please enter the lower limit: "))
            upper_limit = int(input("Please enter the upper limit: "))   
            max_attempts = int(input("Please enter the number of guesses: "))

            try: 
                lower_limit = int(lower_limit)
                upper_limit = int(upper_limit)
                max_attempts = int(max_attempts)

                if lower_limit >= upper_limit:
                    print("The lower limit must be less than the upper limit.")
                
                elif max_attempts <=0 :
                    print("The maximum number of guesses must be positive.")

                else: 
                    return lower_limit, upper_limit, max_attempts
            except ValueError:
                print("Please enter valid numbers.")
    

# user input
def get_guess(lower_limit, upper_limit):
    while True:
        try:   
            guess = int(input(f"Enter a number between {lower_limit} and {upper_limit}: "))
            if guess < lower_limit or guess > upper_limit:
                print(f"Please enter a number between {lower_limit} and {upper_limit}.")
            else: 
                return guess
        except ValueError:
            print("Please enter a valid number.")
        

# check condition from user
def check_guess(guess, secret_number, attempts):
    if guess == secret_number:
        if attempts == 1:
            print("Congratulations! You found the secret number ",secret_number,"in", attempts, "guess!")
        else:
            print("Congratulations! You found the secret number ",secret_number,"in", attempts, "guesses!")
        return True
    elif guess > secret_number:
        print("The secret number is lesser. Go DOWN ↓")
    else:
        print("The secret number is greater. Go UP ↑")
    return False

# central game control 
def play_game():
    limits = set_limits()
    if limits is None:
        return
    lower_limit, upper_limit, max_attempts = limits
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        guess = get_guess(lower_limit, upper_limit)
        if check_guess(guess, secret_number, attempts):
            break
        
    else:
        print(f"Unfortunately the number of guesses ran out... The secret number is {secret_number}. Better luck next time :)")
    

if __name__ == "__main__":
    print("Welcome to the game where you guess the secret number. Good luck!")
    play_game()