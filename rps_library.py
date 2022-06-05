
#USER_INPUT_VALIDATION
def player_input_validation(player_input, game_possible_inputs):    
    player_input = player_input.upper().strip()
    if (player_input not in game_possible_inputs):
        return None
    else:
        return player_input

#CHECK PLACE HOLDER OF INPUTS 
def check_place(game_input_list,game_possible_inputs):
    check_places = list()
    for _ in game_possible_inputs:
        if _ in game_input_list:
            check_places.append(1)
        else:
            check_places.append(0)
    return check_places

#CONFIRM GAME RULES
def game_rules(check_input_places):
    paper = check_input_places[0]
    rock = check_input_places[1]
    scissors = check_input_places[2]
    if (paper and rock):
        return 'P'
    elif (paper and scissors):
        return 'S'
    elif (rock and scissors):
        return 'R'

#CHECK WINNER
def winner_check(player_input,cpu_input, win_ticket):
    if player_input == win_ticket:
        return 'PLAYER'
    elif cpu_input == win_ticket:
        return 'CPU'

#WHAT IS THE INPUT
def what_input(any_input):
    the_input = ''
    if any_input == 'P':
        the_input = 'Paper'
    elif any_input == 'R':
        the_input = 'Rock'
    elif any_input == 'S':
        the_input = 'Scissors'
    return the_input