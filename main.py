import art
import game_data
import random

choice_a, choice_b = "", ""
score = 0

print(art.logo)
print("\nWelcome to Guess-Who-Is-More-Popular game!\n")
print()

# Let's set up a function that would pick a good match from the database.

def pick_choice(choice):
    """Enables selection of a second option that would be different from first option"""
    valid_choice_b = False
    while not valid_choice_b:
        choice = random.choice(game_data.data)
        if choice == choice_a:
            pick_choice(choice)
        else:
            valid_choice_b = True
            return choice


# Here, let us pick the choices to offer to user

game_continues = True
round_counter = 0
choice_a = random.choice(game_data.data)

while game_continues:
    round_counter += 1
    print("===========================================================")
    print(f"\nRound {round_counter} starts.")
    print("Who is more popular? (Hint: type \"A\" or \"B\" to provide answer.)\n")
    # print(choice_a)
    choice_b = pick_choice(choice_b)
    # print(choice_b)
    print(f"{choice_a['name']}, a {choice_a['description']} from {choice_a['country']}, or...\n")
    print(f"{choice_b['name']}, a {choice_b['description']} from {choice_b['country']}?\n")
    selection = input("So, who is more popular? A or B? ").lower()
    if selection == "a" and choice_a['follower_count'] >= choice_b['follower_count']:
        print(f"\nCorrect! {choice_a['name']} has {choice_a['follower_count']} followers, and {choice_b['name']} has {choice_b['follower_count']} followers.")
        print(f"You are advancing to the next round.")
        choice_a = choice_b
        choice_b = pick_choice(choice_b)
    elif selection == "b" and choice_a['follower_count'] <= choice_b['follower_count']:
        print(f"\nCorrect! {choice_a['name']} has {choice_a['follower_count']} followers, and {choice_b['name']} has {choice_b['follower_count']} followers.")
        print(f"You are advancing to the next round.")
        choice_a = choice_b
        choice_b = pick_choice(choice_b)
    else:
        print(f"\nIncorrect! {choice_a['name']} has {choice_a['follower_count']} followers, and {choice_b['name']} has {choice_b['follower_count']} followers.")
        print(f"The game ends now. You have guessed correct {round_counter -1} times. Thank you for playing.")
        game_continues = False