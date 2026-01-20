import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = round((max(poss_values) + min(poss_values))/2)
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if (current_val < next_val) and user_input == 'h':
        return True
    elif (current_val > next_val) and user_input == 'l':
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    in_word = False
    for i in range(len(word)):
        if word[i] == letter:
            board[i] = letter
            in_word = True
    if in_word == True:
        print(f'''Well done! '{letter}' is in the word''')
        return True
    if in_word == False:
        print(f'''Sorry, '{letter}' is not in the word''')
        return False
        

