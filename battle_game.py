import random
import sys
# Defining a function to implement a fresh page feature


def clear_output():
    print('\n'*100)

# Defining a funtion to implement the monster's attack strength
# minimum attack strength = 12 and maximum attack strength = 20


def monster_attack_strength(min_attack, max_attack):
    return random.randint(min_attack, max_attack)

# Defining a function to ask whether the user want to play again or not


def replay():
    return input('Are you ready to continue in this battle ? Enter Yes or No : ').upper().startswith('Y')

# Winner Declared


def game_ends(winner_name):
    print(f'{winner_name} won the game')


# Declaring the game statistics as a global variable
game_stastistics = []
game_on = True
# Defining the main program


while game_on:
    # Game Interface
    print("Welcome to the Battle Game")
    print('---'*7)
    print("\n")
    player = {'name': None, 'health': 100, 'attack': 17, 'heal': 10}
    monster = {'name': "Monster King", 'health': 100,
               'attack_min': 10, 'attack_max': 20}
    player['name'] = input("Hey, Enter your name : ").title()

    round_counter = 0  # Counter for number of rounds played
    # DIsplaying the initial status of the player and the enemy
    print("\nInitial Status of Player and Enemy : \n")
    print(f"Health of {player['name']} = {player['health']} \n")
    print(f"Health of {monster['name']} = {monster['health']} \n")

    play_game = input("Are you ready to play ? Enter Yes or No: ")

    if play_game.upper().startswith('Y'):
        new_round = True

    else:
        # Exiting the game
        new_round = False
        sys.exit()

    # Defining the while loop for new round

    while new_round:

        round_counter += 1
        player_won = False
        monster_won = False

        # Game interface
        print("Select an Action : \n")
        print("1)Attack\n2)Heal\n3)Game Results\n4)Exit game\n")
        option = int(input("Enter your choice ( 1 - 4 ) : "))

        # Attacking

        if option == 1:
            monster['health'] -= player['attack']

            if monster['health'] <= 0:
                player_won = True
            else:
                # Monster fights back the player
                player['health'] -= monster_attack_strength(
                    monster['attack_min'], monster['attack_max'])
                if player['health'] <= 0:
                    monster_won = True

        # Healing the player

        elif option == 2:

            player['health'] += player['heal']
            # Maximum Health  = 100 and the player wouldn't be able to heal when Health is maximum
            if player['health'] >= 100:
                print("Player health can't exceed beyond 100 \n")
                player['health'] = 100

            player['health'] -= monster_attack_strength(
                monster['attack_min'], monster['attack_max'])
            if player['health'] <= 0:
                monster_won = True

        # Displaying the game results
        elif option == 3:

            for player_status in game_stastistics:
                print(player_status)

        # Exiting the game

        elif option == 4:
            game_on = False
            print("Exiting Game !!!")
            sys.exit()

        else:
            print("Invalid Option")

        # Checking the current round's result

        if player_won == False and monster_won == False:
            print(f"Health of {player['name']} = {player['health']} \n")
            print(f"Health of {monster['name']} = {monster['health']} \n")

        elif player_won:
            print("\nCongratulations !!!!\n")
            game_ends(player['name'])
            round_result = {
                'name': player['name'], 'health': player['health'], 'rounds': round_counter}
            game_stastistics.append(round_result)
            new_round = False
        elif monster_won:
            print("\nOops !!!!\n")
            game_ends(monster['name'])
            round_result = {
                'name': monster['name'], 'health': monster['health'], 'rounds': round_counter}
            game_stastistics.append(round_result)
            new_round = False

        if not replay():
            sys.exit()
