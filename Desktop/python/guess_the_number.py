import random

def generate_random_number():
    return random.randint(1,20)

def take_user_guess():
    
    while True:
        try:
            user_input = int(input("enter your guess:"))
            return user_input
        except valueError:
            print("please enter a valid number.")
            
def check_guess(random_number, user_guess):
    if user_guess < random_number:
        print("too low! try a high number.")
    elif user_guess > random_number:
        print("too high! try a lower number.")
    else:
        print("congratulation! you guessed the correct nuber.")
        return True
    return False
def calculate_score(attempts, max_attempts):
    max_score = 100
    if attempts == 1:
        return max_score
    return max (0,max_score - ((attempts - 1)*(max_score / (max_attempts - 1))))
def main():
    print("welcome to the number guessing game!")
    secret_number =generate_random_number()
    
    attempts = 0
    max_attempts = 5
    scored = False
    
    while attempts < max_attempts:
        attempts += 1
        print(f"\nAttempt {attempts} out of {max_attempts}")
        user_guess = take_user_guess()
        
        scored = check_guess(secret_number, user_guess)
        if scored:
            print(f"you've guessed it in {attempts} attempt(s)!")
            score = calculate_score(attempts, max_attempts)
            print(f"your score: {score}")
            break
    else:
        print(f"\nsorry, you've used all {max_attempts} attempts. the number was {secret_number}.")
      
if __name__ =="__main__":
    main()      
                   
        

    
    
