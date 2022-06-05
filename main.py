import random

game_possible_inputs = ['P','R','S']

from rps_library import player_input_validation, check_place, game_rules, winner_check, what_input



while True:
    player_input = player_input_validation(input("ENTER YOUR INPUT (can only be P,R or S)>> "), game_possible_inputs)
    if player_input == None:
        print("ERROR!. THIS IS AN INVALID INPUT. PLEASE TRY AGAIN.")
        continue
    else:
        cpu_input = random.choice(game_possible_inputs)
        print(f"Player ({what_input(player_input)}) : CPU ({what_input(cpu_input)})")        
        if player_input == cpu_input:
            print("IT'S A TIE. PLAY AGAIN")
            continue
        else:        
            game_input_list = [player_input,cpu_input]        
            check_input_places = check_place(game_input_list,game_possible_inputs)
            win_ticket = game_rules(check_input_places)
            winner = winner_check(player_input,cpu_input,win_ticket)
            print(f"{winner} wins!!!")
            break
