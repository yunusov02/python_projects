import random

def main():
    print("Please guess a number between 0 to 100, and I will try to find it.\n")
    limit = 10
    start = 0
    end = 100
    while limit > 0:
        guessedNumber = random.randint(start, end)
        print(f"I think it is {guessedNumber}")
        answer = input("Enter your answer [H, L, C]: ").lower()
        
        if answer == "h":
            end = guessedNumber - 1
        elif answer == "l":
            start = guessedNumber + 1
        elif answer == "c":
            print(f"I win! It was {guessedNumber}.")
            break 
        else:
            print("Invalid input. Please enter 'H', 'L', or 'C'.")
        
        limit -= 1

        if limit == 0:
            print("I ran out of guesses. Better luck next time!")

if __name__ == "__main__":
    main()
