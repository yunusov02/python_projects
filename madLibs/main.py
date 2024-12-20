from random import randint
from story import madlib1, madlib2, madlib3, adjectives, nouns, places, verbs;



def main():
    stories = {
        "1": madlib1,
        "2": madlib2,
        "3": madlib3
    }
    
    n = input("Enter a number between 1 to 3: ")

    if n in stories.keys():
        stories[n]()
    else:
        print("You entered number between 1 to 3")


if __name__ == "__main__":
    main()

