import random

def main():
    guessedNumber = random.randint(0, 100)
    print("I guessed number between 0 and 100\nCan you find it\n")
    limit = 10
    while limit > 0:
        num = int(input("Enter your choice: "))
        if num == guessedNumber:
            print(f"You are right it was {guessedNumber}")
            break
        elif num < guessedNumber:
            print("Too low")
        else:
            print("Too high")
        limit -= 1



if __name__ == "__main__":
    main()

