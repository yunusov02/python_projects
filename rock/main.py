import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer1_choice, computer2_choice):
    choices = {'rock': 0, 'paper': 1, 'scissors': 2}
    
    user = choices[user_choice]
    comp1 = choices[computer1_choice]
    comp2 = choices[computer2_choice]
    
    results = [user, comp1, comp2]
    
    if len(set(results)) == 1:
        return "It's a tie! All chose the same."

    user_vs_comp1 = (user - comp1) % 3
    user_vs_comp2 = (user - comp2) % 3
    comp1_vs_comp2 = (comp1 - comp2) % 3

    if user_vs_comp1 == 1 and user_vs_comp2 == 1:
        return "You win! You beat both computers!"
    elif user_vs_comp1 == 2 and user_vs_comp2 == 2:
        return "You lose! Both computers beat you!"
    elif user_vs_comp1 == 2:
        return "You lose! Computer 1 beats you!"
    elif user_vs_comp2 == 2:
        return "You lose! Computer 2 beats you!"
    elif comp1_vs_comp2 == 2:
        return "Computer 1 beats Computer 2!"
    else:
        return "It’s a tie between the computers!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return
    
    computer1_choice = get_computer_choice()
    computer2_choice = get_computer_choice()
    
    print(f"Computer 1 chooses {computer1_choice}")
    print(f"Computer 2 chooses {computer2_choice}")
    
    result = determine_winner(user_choice, computer1_choice, computer2_choice)
    print(result)

if __name__ == "__main__":
    main()
