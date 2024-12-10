from game import game

def main():
    print("Welcome to the game of 2048")
    print("Use keywords: \n\tW for up \n\tS for down \n\tA for right \n\tD for left")
    
    while True:
        pole_size = int(input("Please enter of pole size (2, 3, 4, 5): "))
        if pole_size >= 2 and pole_size <= 5:
            break
        print("Please enter a number between 2 and 5")

    game(pole_size)


if __name__ == "__main__":
    main()

