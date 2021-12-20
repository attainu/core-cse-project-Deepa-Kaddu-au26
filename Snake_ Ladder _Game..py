# Snake and Ladder Game

# Importing Random Function
import random
import sys


MAX_VAL = 100
DICE_FACE = 6

# Snake takes you down from 'key' to 'value'
snakes = { 8: 4, 26: 10, 51: 6, 56: 1, 75: 28, 85: 59, 92: 25, 99: 63 }

# Ladder takes you up from 'key' to 'value'
ladders = { 3: 20, 11: 28, 17: 74, 38: 59, 57: 76, 73: 86, 81: 98, 88: 91}


# Messages for Player turn, for snake bite and for ladder jump
player_turn_text = ["Your turn.", "Go.", "Please proceed.", "Lets win this.", "Are you ready?", "",]

snake_bite = ["boohoo","bummer","snake bite","oh no","dang"]

ladder_jump = ["woohoo","woww","nailed it","oh my God...","yaayyy"]

#welcome message
print("Welcome to Snake and Ladder Game.")


#Asking Player Names
def get_player_names():
    player1_name = input("Please enter a valid name for first player: ")
    player2_name = input("Please enter a valid name for second player: ")

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name

# For Random Dice Value
def get_dice_value():
    dice_value = random.randint(1, DICE_FACE)
    print("Its a " + str(dice_value))
    return dice_value

#For Printing a message, for snake Bite and displayig the current postition
def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper() + " ~~~~>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))

#For Printing a message, for Ladder jump  and displayig the current postition
def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))

#used if and else condition
def snake_ladder(player_name, current_value, dice_value):
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value

#To check winner
def check_win(player_name, position):
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game.\n\n")
        sys.exit(1)

#To Start Game
def start():
    player1_name, player2_name = get_player_names()


    player1_current_position = 0
    player2_current_position = 0

    while True:
        input_1 = input("\n" + player1_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_value()
        print(player1_name + " moving....")
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

        check_win(player1_name, player1_current_position)

        input_2 = input("\n" + player2_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_value()
        print(player2_name + " moving....")
        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

        check_win(player2_name, player2_current_position)

    
start()