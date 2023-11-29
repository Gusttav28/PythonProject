import os
import random
import readchar

POS_X = 0
POS_Y = 1

MAP_OBSTACLES_WIDHT = 3
MAP_OBSTACLES_HEIGHT = 2
NUM_OF_OBJECTS = 20
PIKACHU_INITIAL_LIFE = 80
pikachu_life = PIKACHU_INITIAL_LIFE
SQUIRTLE_INITIAL_LIFE = 90
squirtle_life = SQUIRTLE_INITIAL_LIFE
VEGETA_LIFE = 85
vegeta_life = VEGETA_LIFE
THANOS_LIFE = 90
thanos_life = THANOS_LIFE
SUPERMAN_LIFE = 95
superman_life = SUPERMAN_LIFE
bosses_list = [pikachu_life, vegeta_life, thanos_life, superman_life]
user = " @ "

obstacles_defination = """\
###########################
# []                      #
#                         #
#                         #
#                         #
#                         #        
#                         #
#                         #
#                         #
#                         #
#                         #
#                         #
#                         #
#                         #
#                         #
###########################\
"""

my_position = [0, 1]
map_objects = []
tail = []
tail_length = 0
lines_down = "-"

end_game = False
end_pikachus_game = False
died = False
user_game_rules = False
object_in_cell_game = False

# Create obstacles maps

obstacles_defination = [list(row) for row in obstacles_defination.split("\n")]
MAP_WIDTH = len(obstacles_defination[0])
MAP_HEIGHT = len(obstacles_defination)

# Welcome to the user for the game
user_welcome = "¡WELCOME TO MY PIKACHU'S GAME VERSION TWO!"
print("\n" + user_welcome + "\n" + lines_down * len(user_welcome) + "\n")
user_continue_to_the_game = input("Press enter to continue and skip the rules, or press [N] to see this rules... \n")
if user_continue_to_the_game == "n":
    rules = input("ALRIGHT THIS ARE GONNA BE THE RULES: \n")
    print("\n" + rules + "\n" + lines_down * len(rules) + "\n")
    announcement_rules = input("So the game it's about pikachu right, well the @ it's gonna be you (pikachu)\n"
                               "You're gonna pass to every obstacle in the map but every time that you're in some abstacle \n"
                               "They are gonna some bosses That you have to defeat so, are you ready? [Y/N]: \n")
    if announcement_rules == "y":
        user_continue = input("Alright, good luck!! [Press enter] \n")




# Main Loop
while not end_game and not end_pikachus_game:
    os.system("clear")

    # Generates ramdon objects on the map
    while len(map_objects) < NUM_OF_OBJECTS:
        new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

        if new_position not in map_objects and new_position != my_position and \
                obstacles_defination[new_position[POS_Y]][new_position[POS_X]] != "#":
            map_objects.append(new_position)



    print("+" + "-" * (MAP_WIDTH) * 2 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):


            char_to_draw = "  "
            object_in_cell = []
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_Y] == coordinate_x and map_object[POS_X] == coordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_object 

            
            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = " @"
                    tail_in_cell = tail_piece

 
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"
                
                        # PIKACHU, VEGETA, THANOS AND SUOERMAN FIGHT'S
                def fight_pikachu_life(pikachu_life):
                    global squirtle_life

                    if pikachu_life:


                        pikachu_boss = "YOU ARE GONNA STAR TO FIGHT WITH PIKACHU [Press enter to continue]"
                        print("\n" + pikachu_boss + "\n" + lines_down * len(pikachu_boss) + "\n")
                        input("LET THE FIGHT BEGIN!")
                        os.system("clear")
                
                            #  PIKACHUS - SQUIRTLE FIGHT LOOP
                        while not end_game and pikachu_life > 0 and squirtle_life > 0:
                            os.system("clear")
                                            # PIKACHU'S TURN      
                            pikachu_turn = "PIKACHU'S TURN"
                            print("\n" + pikachu_turn + "\n" + lines_down * len(pikachu_turn) + "\n")
                            pikachu_stroke = random.randint(1, 2)
                            if pikachu_stroke == 1:
                                    # volt ball
                                pikachu_stroke_volt_ball = input("PIKACHU ATTACK WITH VOLT BALL")
                                print("\n" + pikachu_stroke_volt_ball + "\n" + lines_down * len(pikachu_stroke_volt_ball) + "\n")
                                squirtle_life -= 10
                            else:         #thunder shot
                                pikachu_stroke_thunder_shot = input("PIKACHU ATTAKS WITH THUNDER SHOT")
                                print("\n" + pikachu_stroke_thunder_shot + "\n" + lines_down * len(pikachu_stroke_thunder_shot) + "\n")
                                squirtle_life -= 11
                    
                            if pikachu_life < 0:
                                pikachu_life = 0
                            if squirtle_life < 0:
                                squirtle_life = 0

                            os.system("clear")

                            print("PIKACHU LIFE IS: " + "\n" + "[" + "#" * pikachu_life + "]"  " ({}/{})".format(pikachu_life,PIKACHU_INITIAL_LIFE) + "\n"    \
                                "SQUIRTLE LIFE IS: " + "\n" + "[" + "#" * squirtle_life + "]" " ({}/{})".format(squirtle_life, SQUIRTLE_INITIAL_LIFE) + "\n") 

                            input("Press enter to continue...")
                            os.system("clear")
                    
                                #  SQUIRTLE'S TURN
                            squirtle_turn = "SQUIRTLE'S TURN"
                            print("\n" + squirtle_turn + "\n" + lines_down * len(squirtle_turn) + "\n")
                            squirtle_stroke = None
                            while squirtle_stroke not in ["a", "b", "c", "d", "q"]:
                                squirtle_stroke = input("Which attack do you wanna use: \n"
                                                        "\n A Tackle \n"
                                                        "\n B Water gun \n"
                                                        "\n C Bubble \n"
                                                        "\n D No attack \n"
                                                        "\n Q For go out of the game \n"
                                                        "\n A, B, C, D?: \n")
                                if squirtle_stroke == "a":
                                    squirtle_stroke_tackle = "SQUIRTLE ATTACK WITH TACKLE"
                                    print("\n" + squirtle_stroke_tackle + "\n" + lines_down * len(squirtle_stroke_tackle) + "\n")
                                    pikachu_life -= 10
                                elif squirtle_stroke == "b":
                                    squirtle_stroke_water_gun = "SQUIRLTE ATTACK WITH TACKLE"
                                    print("\n" + squirtle_stroke_water_gun + "\n" + lines_down * len(squirtle_stroke_water_gun) + "\n")
                                    pikachu_life -= 12
                                elif squirtle_stroke == "c":
                                    squirtle_stroke_bubble = "SQUIRLTE ATTACK WITH BUBBLE"
                                    print("\n" + squirtle_stroke_bubble + "\n" + lines_down * len(squirtle_stroke_bubble) + "\n")
                                    pikachu_life -= 9
                                elif squirtle_stroke == "d":
                                    squirtle_stroke_no_attack = "SQUIRLTE DECIDES NO ATTACK"
                                    print("\n" + squirtle_stroke_no_attack + "\n" + lines_down * len(squirtle_stroke_no_attack) + "\n")
                            
                        
                                if pikachu_life < 0:
                                    pikachu_life = 0
                                if squirtle_life < 0:
                                    squirtle_life = 0

                                os.system("clear")

                                print("PIKACHU LIFE IS: " + "\n" + "[" + "#" * pikachu_life + "]"  " ({}/{})".format(pikachu_life,PIKACHU_INITIAL_LIFE) + "\n"    \
                                    "SQUIRTLE LIFE IS: " + "\n" + "[" + "#" * squirtle_life + "]" " ({}/{})".format(squirtle_life, SQUIRTLE_INITIAL_LIFE) + "\n") 

                                input("Press enter to continue...")
                                os.system("clear")
                        

                        
                        if end_game:
                            print("You press [Q] to go out of the game")

                        if squirtle_life > pikachu_life:
                            return True                
                        else:
                            return False
                

                        # VEGETA FIGHT
                def fight_vegeta_life(vegeta_life):
                    global squirtle_life

                    if vegeta_life:
                        vegeta_boss = "YOU ARE GONNA STAR TO FIGHT WITH VEGETA [Press enter to continue]"
                        print("\n" + vegeta_boss + "\n" + lines_down * len(vegeta_boss) + "\n")
                        input("LET THE FIGHT BEGIN!")
                        os.system("clear")

                                          #  VEGETA - SQUIRTLE FIGHT LOOP
                        while not end_game and vegeta_life > 0 and squirtle_life > 0:
                            os.system("clear")
                            vegeta_turn = "VEGETA TURN"
                            print("\n" + vegeta_turn + "\n" + lines_down * len(vegeta_turn) + "\n")
                            vegeta_stroke = random.randint(1, 2)
                            if vegeta_stroke == 1:
                                    #  POWER BALL
                                power_ball = "VEGETA ATTACKS WITH POWER BALL"
                                print("\n" + power_ball + "\n" + lines_down * len(power_ball) + "\n")
                                squirtle_life -= 12
                            elif vegeta_stroke == 2:
                                    # COSMIC CANNON
                                cosmic_cannon = "VEGETA ATTACKS WITH COSMIC CANNON"
                                print("\n" + cosmic_cannon + "\n" + lines_down * len(cosmic_cannon) + "\n")
                                squirtle_life -= 11
                            else:
                                    # FINAL FLASH
                                final_flash = "VEGETA ATTACKS WITH FINAL FLAS"
                                print("\n" + final_flash + "\n" + lines_down * len(final_flash) + "\n")
                                squirtle_life -= 15
                            
                            if vegeta_life < 0:
                                vegeta_life = 0                            
                            if squirtle_life < 0:
                                squirtle_life = 0

                            os.system("clear")

                            print("VEGETA LIFE IS: " + "\n" + "[" + "#" * vegeta_life + "]"  " ({}/{})".format(vegeta_life,VEGETA_LIFE) + "\n"    \
                                  "SQUIRTLE LIFE IS: " + "\n" + "[" + "#" * squirtle_life + "]" " ({}/{})".format(squirtle_life, SQUIRTLE_INITIAL_LIFE) + "\n") 

                            input("Press enter to continue...")
                            os.system("clear")

                                                            #  SQUIRTLE'S TURN
                            squirtle_turn = "SQUIRTLE'S TURN"
                            print("\n" + squirtle_turn + "\n" + lines_down * len(squirtle_turn) + "\n")
                            squirtle_stroke = None
                            while squirtle_stroke not in ["a", "b", "c", "d", "q"]:
                                squirtle_stroke = input("Which attack do you wanna use: \n"
                                                        "\n A Tackle \n"
                                                        "\n B Water gun \n"
                                                        "\n C Bubble \n"
                                                        "\n D No attack \n"
                                                        "\n Q For go out of the game \n"
                                                        "\n A, B, C, D?: \n")
                                if squirtle_stroke == "a":
                                    squirtle_stroke_tackle = "SQUIRTLE ATTACK WITH TACKLE"
                                    print("\n" + squirtle_stroke_tackle + "\n" + lines_down * len(squirtle_stroke_tackle) + "\n")
                                    vegeta_life -= 10
                                elif squirtle_stroke == "b":
                                    squirtle_stroke_water_gun = "SQUIRLTE ATTACK WITH TACKLE"
                                    print("\n" + squirtle_stroke_water_gun + "\n" + lines_down * len(squirtle_stroke_water_gun) + "\n")
                                    vegeta_life -= 12
                                elif squirtle_stroke == "c":
                                    squirtle_stroke_bubble = "SQUIRLTE ATTACK WITH BUBBLE"
                                    print("\n" + squirtle_stroke_bubble + "\n" + lines_down * len(squirtle_stroke_bubble) + "\n")
                                    vegeta_life -= 8
                                elif squirtle_stroke == "d":
                                    squirtle_stroke_no_attack = "SQUIRLTE DECIDES NO ATTACK"
                                    print("\n" + squirtle_stroke_no_attack + "\n" + lines_down * len(squirtle_stroke_no_attack) + "\n")
                            
                        
                                if vegeta_life < 0:
                                    vegeta_life = 0
                                if squirtle_life < 0:
                                    squirtle_life = 0

                                os.system("clear")

                                print("VEGETA LIFE IS: " + "\n" + "[" + "#" * vegeta_life + "]"  " ({}/{})".format(vegeta_life,VEGETA_LIFE) + "\n"    \
                                      "SQUIRTLE LIFE IS: " + "\n" + "[" + "#" * squirtle_life + "]" " ({}/{})".format(squirtle_life, SQUIRTLE_INITIAL_LIFE) + "\n") 

                                input("Press enter to continue...")
                                os.system("clear")
                        

                        
                        if end_game:
                            print("You press [Q] to go out of the game")

                        if squirtle_life > vegeta_life:
                            return True                
                        else:
                            return False
                         
                        # THANOS FIGHT                            
                def fight_thanos_life(thanos_life):
                    global squirtle_life

                    if thanos_life:
                        thanos_boss = "YOU'RE GONNA STAR TO FIGHT WITH THANOS [Press enter to continue...]"
                        print("\n" + thanos_boss + "\n" + lines_down * len(thanos_boss) + "\n")
                        input("LET THE FOGHT BEGIN")
                        os.system("clear")

                            # THANOS - SQUIRTLE FIGHT
                        while not end_game and thanos_life > 0 and squirtle_life > 0:
                                # THANOS TURN
                            thanos_turn = "THANOS TURN"
                            print("\n" + thanos_turn + "\n" + lines_down * len(thanos_turn) + "\n")
                            thanos_stroke = random.randint(1, 2)
                            if thanos_stroke == 1:
                                # COMBINED ENERGY BALL
                                thanos_attack_energy_ball = "THANOS ATTACK WITH COMBINED ENERGY BALL"
                                print("\n" + thanos_attack_energy_ball + "\n" + lines_down * len(thanos_attack_energy_ball) + "\n")
                                squirtle_life -= 14
                                # FIRE BREATH
                            elif thanos_stroke == 2:
                                thanos_attak_fire_breath = "THANOS ATTACKS WITH FIRE BREATH"
                                print("\n" + thanos_attak_fire_breath + "\n" + lines_down * len(thanos_attak_fire_breath) + "\n")
                                squirtle_life -= 12
                                # CHAOTIC CANYON
                            else:
                                thanos_attak_chaotic_canyon = "THANOS ATTACKS WITH CHAOTIC CANYON"
                                print("\n" + thanos_attak_chaotic_canyon + "\n" + lines_down * len(thanos_attak_chaotic_canyon) + "\n")
                                squirtle_life -= 15

                            
                            if thanos_life < 0:
                                thanos_life = 0
                            if squirtle_life < 0:
                                squirtle_life = 0

                            os.system("clear")

                            print("THANOS LIFE IS: " + "\n" + "[" + "#" * thanos_life + "]"  " ({}/{})".format(thanos_life,THANOS_LIFE) + "\n"    \
                                  "SQUIRTLE LIFE IS: " + "\n" + "[" + "#" * squirtle_life + "]" " ({}/{})".format(squirtle_life, SQUIRTLE_INITIAL_LIFE) + "\n") 
                            
                            input("Press enter to continue...")
                            os.system("clear")
                            
                                                           #  SQUIRTLE'S TURN
                            squirtle_turn = "SQUIRTLE'S TURN"
                            print("\n" + squirtle_turn + "\n" + lines_down * len(squirtle_turn) + "\n")
                            squirtle_stroke = None
                            while squirtle_stroke not in ["a", "b", "c", "d", "q"]:
                                squirtle_stroke = input("Which attack do you wanna use: \n"
                                                        "\n A Tackle \n"
                                                        "\n B Water gun \n"
                                                        "\n C Bubble \n"
                                                        "\n D No attack \n"
                                                        "\n Q For go out of the game \n"
                                                        "\n A, B, C, D?: \n")
                                if squirtle_stroke == "a":
                                    squirtle_stroke_tackle = "SQUIRTLE ATTACK WITH TACKLE"
                                    print("\n" + squirtle_stroke_tackle + "\n" + lines_down * len(squirtle_stroke_tackle) + "\n")
                                    thanos_life -= 10
                                elif squirtle_stroke == "b":
                                    squirtle_stroke_water_gun = "SQUIRLTE ATTACK WITH TACKLE"
                                    print("\n" + squirtle_stroke_water_gun + "\n" + lines_down * len(squirtle_stroke_water_gun) + "\n")
                                    thanos_life -= 12
                                elif squirtle_stroke == "c":
                                    squirtle_stroke_bubble = "SQUIRLTE ATTACK WITH BUBBLE"
                                    print("\n" + squirtle_stroke_bubble + "\n" + lines_down * len(squirtle_stroke_bubble) + "\n")
                                    thanos_life -= 12
                                elif squirtle_stroke == "d":
                                    squirtle_stroke_no_attack = "SQUIRLTE DECIDES NO ATTACK"
                                    print("\n" + squirtle_stroke_no_attack + "\n" + lines_down * len(squirtle_stroke_no_attack) + "\n")
                            
                        
                                if thanos_life < 0:
                                    thanos_life = 0
                                if squirtle_life < 0:
                                    squirtle_life = 0

                                os.system("clear")

                                print("THANOS LIFE IS: " + "\n" + "[" + "#" * thanos_life + "]"  " ({}/{})".format(thanos_life,THANOS_LIFE) + "\n"    \
                                      "SQUIRTLE LIFE IS: " + "\n" + "[" + "#" * squirtle_life + "]" " ({}/{})".format(squirtle_life, SQUIRTLE_INITIAL_LIFE) + "\n") 

                                input("Press enter to continue...")
                                os.system("clear")
                        

                        
                        if end_game:
                            print("You press [Q] to go out of the game")

                        if squirtle_life > thanos_life:
                            return True                
                        else:
                            return False

                        # SUPER MAN FINAL FIGHT                
                def fight_superman_life(superman_life):
                    global squirtle_life                    

                    if superman_life:
                        
                        superman_boss = "YOU'RE GONNA STAR TO FIGHT WITH SUPERMAN [Press enter to continue...]"
                        print("\n" + superman_boss + "\n" + lines_down * len(superman_boss) + "\n")
                        input("LET THE FIGHT BEGIN")
                        os.system("clear")
                         
                                    # SUPERMAN - SQUIRTLE FIGHT
                        while not end_game and superman_life > 0 and squirtle_life > 0:
                                        # SUPERMAN TURM
                            superman_turn = "SUPERMAN TURN'S"
                            print("\n" + superman_turn + "\n" + lines_down * len(superman_turn) + "\n")
                            superman_strock = random.randint(1, 2)
                            if superman_strock == 1:
                                        # FIGHT SPEED
                                superman_attack_fight_speed = "SUPERMAN ATTACK WITH FIGHT SPEED"
                                print("\n" + superman_attack_fight_speed + "\n" + lines_down * len(superman_attack_fight_speed) + "\n")
                                squirtle_life -= 15
                                        # X-RAY VISION
                            elif superman_strock == 2:
                                superman_attack_xray_vision = "SUPERMAN ATTACK WITH X-RAY VISION"
                                print("\n" + superman_attack_xray_vision + "\n" + lines_down * len(superman_attack_xray_vision) + "\n")
                                squirtle_life -= 12
                                        # FINAL STRIKE  
                            else:
                                superman_attack_final_strike = "SUPERMAN ATTACK WITH FINAL STRIKE"
                                print("\n" + superman_attack_final_strike + "\n" + lines_down * len(superman_attack_final_strike) + "\n")
                                squirtle_life -= 18

                            
                            if superman_life < 0:
                                superman_life = 0
                            if squirtle_life < 0:
                                squirtle_life = 0

                            os.system("clear")

                            print("SUPERMAN LIFE IS: " + "\n" + "[" + "#" * superman_life + "]"  " ({}/{})".format(superman_life,SUPERMAN_LIFE) + "\n"    \
                                "SQUIRTLE LIFE IS: " + "\n" + "[" + "#" * squirtle_life + "]" " ({}/{})".format(squirtle_life, SQUIRTLE_INITIAL_LIFE) + "\n") 
                            
                            input("Press enter to continue...")
                            os.system("clear")

                                        #  SQUIRTLE'S TURN
                            squirtle_turn = "SQUIRTLE'S TURN"
                            print("\n" + squirtle_turn + "\n" + lines_down * len(squirtle_turn) + "\n")
                            squirtle_stroke = None
                            while squirtle_stroke not in ["a", "b", "c", "d", "q"]:
                                squirtle_stroke = input("Which attack do you wanna use: \n"
                                                        "\n A Tackle \n"
                                                        "\n B Water gun \n"
                                                        "\n C Bubble \n"
                                                        "\n D No attack \n"
                                                        "\n Q For go out of the game \n"
                                                        "\n A, B, C, D?: \n")
                                if squirtle_stroke == "a":
                                    squirtle_stroke_tackle = "SQUIRTLE ATTACK WITH TACKLE"
                                    print("\n" + squirtle_stroke_tackle + "\n" + lines_down * len(squirtle_stroke_tackle) + "\n")
                                    superman_life -= 15
                                elif squirtle_stroke == "b":
                                    squirtle_stroke_water_gun = "SQUIRLTE ATTACK WITH TACKLE"
                                    print("\n" + squirtle_stroke_water_gun + "\n" + lines_down * len(squirtle_stroke_water_gun) + "\n")
                                    superman_life -= 12
                                elif squirtle_stroke == "c":
                                    squirtle_stroke_bubble = "SQUIRLTE ATTACK WITH BUBBLE"
                                    print("\n" + squirtle_stroke_bubble + "\n" + lines_down * len(squirtle_stroke_bubble) + "\n")
                                    superman_life -= 12
                                elif squirtle_stroke == "d":
                                    squirtle_stroke_no_attack = "SQUIRLTE DECIDES NO ATTACK"
                                    print("\n" + squirtle_stroke_no_attack + "\n" + lines_down * len(squirtle_stroke_no_attack) + "\n")
                            
                        
                                if superman_life < 0:
                                    superman_life = 0
                                if squirtle_life < 0:
                                    squirtle_life = 0

                                os.system("clear")

                                print("SUPERMAN LIFE IS: " + "\n" + "[" + "#" * superman_life + "]"  " ({}/{})".format(superman_life,SUPERMAN_LIFE) + "\n"    \
                                    "SQUIRTLE LIFE IS: " + "\n" + "[" + "#" * squirtle_life + "]" " ({}/{})".format(squirtle_life, SQUIRTLE_INITIAL_LIFE) + "\n") 

                                input("Press enter to continue...")
                                os.system("clear")
                        
                        if end_game:
                            print("You press [Q] to go out of the game")

                        if squirtle_life > superman_life:
                            return True                
                        else:
                            return False


                if object_in_cell:
                    map_objects.remove(object_in_cell)  
                    tail_length += 1  
                    os.system("clear")
                    

                    if bosses_list:
                        if pikachu_life:
                            squirtle_wins = fight_pikachu_life(pikachu_life)  
                            print("SQUIRTLE WIN!! GOOD JOB, YOU'RE READY TO FIGHT WITH THE NEXT BOSS")                            
                            pikachu_life = bosses_list.remove(pikachu_life)
                            squirtle_life = SQUIRTLE_INITIAL_LIFE
                        elif pikachu_life:
                            print("YOU LOSS TO PIKACHU")
                            end_game = True
                        elif vegeta_life:
                            squirtle_wins = fight_vegeta_life(vegeta_life)
                            print("SQUIRTLE WIN!! GOOD JOB, YOU'RE READY TO FIGHT WITH THE NEXT BOSS")
                            vegeta_life = bosses_list.remove(vegeta_life)                           
                            squirtle_life = SQUIRTLE_INITIAL_LIFE
                        elif vegeta_life:
                            print("YOU LOSS TO VEGETA")
                            end_game = True
                        elif thanos_life:
                            squirtle_wins = fight_thanos_life(thanos_life)
                            print("SQUIRTLE WIN!! GOOD JOB, YOU'RE READY TO FIGHT WITH THE NEXT BOSS")
                            thanos_life = bosses_list.remove(thanos_life)
                            squirtle_life = SQUIRTLE_INITIAL_LIFE
                        elif thanos_life:
                            print("YOU LOSS TO THANOS")
                            end_game = True
                        elif superman_life:
                            squirtle_wins = fight_superman_life(superman_life)
                            print("SQUIRTLE WIN!! GOOD JOB!!")
                            superman_life = bosses_list.remove(superman_life)
                            squirtle_life = SQUIRTLE_INITIAL_LIFE
                        elif superman_life:
                            print("You loss to superman")
                            end_game = True
                    if not bosses_list:
                        congratulations_finish = "CONGRATULATIONS! YOU DEFEATED ALL THE BOSSES. YOU FINISH THE GAME!"
                        print("\n" + congratulations_finish + "\n" + lines_down * len(congratulations_finish) + "\n")
                        end_pikachus_game = True
                        
                if tail_in_cell:
                    end_game = True
                    died = True



            if obstacles_defination[coordinate_y][coordinate_x] == "#":
                char_to_draw = "[]"



            print("{}".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * (MAP_WIDTH) * 2 + "+")

    
    directions = readchar.readchar()

    new_position = None

    if directions == "w":
       new_position = [my_position[POS_X], (my_position[POS_Y] -1) % MAP_WIDTH]

    elif directions == "s":
       new_position = [my_position[POS_X], (my_position[POS_Y] +1) % MAP_WIDTH]

    elif directions == "d":
       new_position = [(my_position[POS_X] +1) % MAP_WIDTH, my_position[POS_Y]]

    elif directions == "a":
       new_position = [(my_position[POS_X] -1) % MAP_WIDTH, my_position[POS_Y]]

    elif directions == "q":
         end_game = True

    if new_position:
        if obstacles_defination[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position

if died:
    print("You collided with yourself, you're dead")
elif end_game:
    print("You press [Q] so you left the game")

