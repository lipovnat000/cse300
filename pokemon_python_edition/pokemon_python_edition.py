import random
import math
import csv
from type_advantages import type_matchups


#name, level, type1, type2, base_hp, base_attack, attack_mod, base_defense, def_mod, base_sp_attack, sp_attack_mod, base_sp_defense, sp_def_mod, base_speed, spd_mod, status, move_1_key, move_2_key, move_3_key, move_4_key
pokemon_dictionary = {"blastoise": ("Blastoise", 50, "Water", "None", 79, 83, 0, 100, 0, 85, 0, 105, 0, 78, 0, "None", "Hydro Pump", "Withdraw", "Aqua Tail", "Tail Whip"),
                      "talonflame": ("Talonflame", 66, "Fire", "Flying", 78, 81, 0, 71, 0, 74, 0, 69, 0, 126, 0, "None", "Aerial Ace", "Agility", "Swords Dance", "Flamethrower")}

ref_name = 0
ref_level = 1
ref_type_1 = 2
ref_type_2 = 3
ref_base_hp = 4
ref_base_attack = 5
ref_attack_mod = 6
ref_base_defense = 7
ref_def_mod = 8
ref_base_sp_attack = 9
ref_sp_attack_mod = 10
ref_base_sp_defense = 11
ref_sp_def_mod = 12
ref_base_speed = 13
ref_spd_mod = 14
ref_status = 15
ref_move_1_key = 16
ref_move_2_key = 17
ref_move_3_key = 18
ref_move_4_key = 19


attack_ref_name = 0
attack_ref_type = 1
attack_ref_accuracy = 2
attack_ref_target = 3
attack_ref_category = 4
attack_ref_power = 5
attack_ref_stat_change = 6
attack_ref_stat_change_level = 7
attack_ref_status_condition = 8
attack_ref_status_condition_chance = 9

pokemon_keys = ("Blastoise", "Talonflame")

def calculate_hp(base_hp, level):
    hp = math.ceil((((2 * base_hp) + 31 + (21 * level))/100) + level + 10)

    return hp

def determine_health_bar(current_hp, max_hp):
    health_percent = float(current_hp/max_hp*100)

    health_remaining_sections = int(math.ceil(health_percent / 5))
    health_lost_sections = int(20 - health_remaining_sections)

    health_bar = "("

    for _ in range(health_remaining_sections):
        health_bar = health_bar + "="
    
    for _ in range(health_lost_sections):
        health_bar = health_bar + "-"

    health_bar = health_bar + ")"

    return health_bar

def set_move(move_key):
    move = None
    with open("moves.csv", 'rt') as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:
            if move_key == row[0]:
                move = row
                break
                
                
    return move

def calculate_non_hp_stat(stat_name, base_stat, level, modifier, status):
    if modifier == 0:
        stat = (((2 * base_stat) + 31 + (21 * level))/100) + 5
    elif modifier > 0:
        stat = ((((2 * base_stat) + 31 + (21 * level))/100) + 5) * ((modifier + 2)/2)
    elif modifier < 0:
        stat = ((((2 * base_stat) + 31 + (21 * level))/100) + 5) * (2/(abs(modifier) + 2))
        
    if (status == "Paralyzed") and (stat_name == "Speed"):
        stat = stat/2

    if (status == "Burned") and (stat_name == "Attack"):
        stat = stat/2
    
    return stat

def print_health_bars():
    player_health_bar = determine_health_bar(player_current_hp, player_max_hp)
    computer_health_bar = determine_health_bar(computer_current_hp, computer_max_hp)

    if (player_pokemon[ref_status] == "None") and (computer_pokemon[ref_status] == "None"):
        print(f"""
                                    {computer_pokemon[ref_name]}
                                    {computer_health_bar} ({computer_current_hp}/{computer_max_hp})


{player_pokemon[ref_name]}
{player_health_bar} ({player_current_hp}/{player_max_hp})""")
    

def execute_move(action, attacking_pokemon, defending_pokemon):
    multiplier = 1
    multiplier = multiplier * float(type_matchups(attacking_pokemon[ref_type_1], defending_pokemon[ref_type_1]))
    if defending_pokemon[ref_type_2] != "None":
        multiplier = multiplier * float(type_matchups(attacking_pokemon[ref_type_1], defending_pokemon[ref_type_2]))
    if attacking_pokemon[ref_type_2] != "None":
        multiplier = multiplier * float(type_matchups(attacking_pokemon[ref_type_2], defending_pokemon[ref_type_1]))
    if (attacking_pokemon[ref_type_2] != "None") and (defending_pokemon[ref_type_2] != "None"):
        multiplier = multiplier * float(type_matchups(attacking_pokemon[ref_type_2], defending_pokemon[ref_type_2]))

    stab = 1
    if (attacking_pokemon[ref_type_1] == action[attack_ref_type]) or (attacking_pokemon[ref_type_2] == action[attack_ref_type]):
        stab = 2

    accuracy_check = random.randrange(100)


    if accuracy_check <= int(action[attack_ref_accuracy]):
        if action[attack_ref_target] == "Opponent":
            if action[attack_ref_category] == "Physical":
                attacking_pokemon_attack = calculate_non_hp_stat("Attack", attacking_pokemon[ref_base_attack], attacking_pokemon[ref_level], attacking_pokemon[ref_attack_mod], attacking_pokemon[ref_status])
                defending_pokemon_defense = calculate_non_hp_stat("Attack", defending_pokemon[ref_base_defense], defending_pokemon[ref_level], defending_pokemon[ref_def_mod], defending_pokemon[ref_status])
            if action[attack_ref_category] == "Special":
                attacking_pokemon_attack = calculate_non_hp_stat("Attack", attacking_pokemon[ref_base_attack], attacking_pokemon[ref_level], attacking_pokemon[ref_sp_attack_mod], attacking_pokemon[ref_status])
                defending_pokemon_defense = calculate_non_hp_stat("Attack", defending_pokemon[ref_base_sp_defense], defending_pokemon[ref_level], defending_pokemon[ref_sp_def_mod], defending_pokemon[ref_status])    
        if (action[attack_ref_target] == "Self") or (action[attack_ref_category] == "Status"):
            # Temporary until program is finished
            print("Oops! The attack failed. Maybe the programmer hasn't finished it yet....")
        if action[attack_ref_category] != "Status":
            damage = math.ceil(((((2 * int(attacking_pokemon[ref_level]) / 5 + 2) * attacking_pokemon_attack * int(action[attack_ref_power]) / defending_pokemon_defense) / 50) + 2) * stab * multiplier * random.randrange(100) / 100)

            global computer_current_hp
            computer_current_hp -= damage

            print(f"{attacking_pokemon[ref_name]} used {action[attack_ref_name]}!")

            if multiplier < 1:
                print("It's not very effective...")
            if multiplier > 1:
                print("It's super effective!")
            if multiplier == 0:
                print("It doesn't affect the opposing pokemon...")
    else:
        print(f"The opposing {defending_pokemon[ref_name]} avoided the attack!")


    
    print()



    global computer_pokemon

    if computer_current_hp <= 0:
        print(f"The opposing {computer_pokemon[ref_name]} fainted.")

    return

def player_turn():
    player_action = "None"
    while player_action not in (player_move_1[attack_ref_name], player_move_2[attack_ref_name], player_move_3[attack_ref_name], player_move_4[attack_ref_name]):
        player_action = input(f"""What will {player_pokemon[ref_name]} do?    
{player_move_1[attack_ref_name]}        {player_move_2[attack_ref_name]}
{player_move_3[attack_ref_name]}        {player_move_4[attack_ref_name]}

""")

        if player_action not in (player_move_1[attack_ref_name], player_move_2[attack_ref_name], player_move_3[attack_ref_name], player_move_4[attack_ref_name]):
            print(f"Oops! {player_pokemon[ref_name]} didn't understand your command")

    if player_action == player_move_1[attack_ref_name]:
        player_action = player_move_1
    if player_action == player_move_2[attack_ref_name]:
        player_action = player_move_2
    if player_action == player_move_3[attack_ref_name]:
        player_action = player_move_3
    if player_action == player_move_4[attack_ref_name]:
        player_action = player_move_4

    execute_move(player_action, player_pokemon, computer_pokemon)

    return



def main():
    while (player_current_hp > 0) and (computer_current_hp > 0):
        turn_order = calculate_non_hp_stat("Speed", player_pokemon[ref_base_speed], player_pokemon[ref_level], player_pokemon[ref_spd_mod], player_pokemon[ref_status]) - calculate_non_hp_stat("Speed", computer_pokemon[ref_base_speed], computer_pokemon[ref_level], computer_pokemon[ref_spd_mod], computer_pokemon[ref_status])
        if turn_order > 0:
            print_health_bars()
            print()
            player_turn()
            #computer_turn
        if turn_order < 0:
            print_health_bars()
            print()
            # computer_turn
            player_turn()
        if turn_order == 0:
            random_turn = random.choice([0,1])
            if random_turn == 0:
                print_health_bars()
                print()
                player_turn()
                #computer_turn
            else:
                print_health_bars()
                print()
                # computer_turn
                player_turn()

    print("The battle ended!")


# SET POKEMON AS GLOBAL VARIABLES

valid_pokemon = False

# Promt user to choose their pokemon out of the available list of keys
while valid_pokemon == False:
    try: 
        print("Choose your Pokemon:")
        for i in pokemon_keys:
            print(f"  {i}")
        print()
        player_pokemon = pokemon_dictionary[input("").lower()]

        valid_pokemon = True

    except KeyError:
        print("That's not a valid Pokemon, please try again")

# Set computer Pokemon
computer_pokemon = pokemon_dictionary[random.choice(pokemon_keys).lower()]

# Set movesets
player_move_1 = set_move(player_pokemon[ref_move_1_key])
player_move_2 = set_move(player_pokemon[ref_move_2_key])
player_move_3 = set_move(player_pokemon[ref_move_3_key])
player_move_4 = set_move(player_pokemon[ref_move_4_key])

computer_move_1 = set_move(computer_pokemon[ref_move_1_key])
computer_move_2 = set_move(computer_pokemon[ref_move_2_key])
computer_move_3 = set_move(computer_pokemon[ref_move_3_key])
computer_move_4 = set_move(computer_pokemon[ref_move_4_key])


# Calculate max HP amounts and set current HP to max to begin with
player_max_hp = calculate_hp(player_pokemon[ref_base_hp], player_pokemon[ref_level])
player_current_hp = player_max_hp
computer_max_hp = calculate_hp(computer_pokemon[ref_base_hp], computer_pokemon[ref_level])
computer_current_hp = computer_max_hp


if __name__ == "__main__":
    main()
