import json
import os

#where is the parent directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

#what is the path to the external file
file_location = os.path.join(script_dir, "mult.json")



print("welcome to the sensetivity converter \n")


game = input("what is your main game: ")
dpi = int(input("what is your dpi: "))
sens = float(input("what is your sens? "))

game_convert = input("what game do you want the sens for? ")

#takes data from external file using the path to it
with open(file_location, "r") as data:
    game_multipliers = json.load(data)

# converts the sens into real world distance
if game in game_multipliers:
    selected_game = game_multipliers[game]
    deg_per_inch = dpi*sens*selected_game
    per_360 = (360 / deg_per_inch) * 2.54
    print(f"your current 360` is: {per_360}")
    
    # converts the sens into a diffrent game
    if game_convert in game_multipliers:
        converted_game = game_multipliers[game_convert]
        new_sens = deg_per_inch / (dpi * converted_game)
        print(f"\nyour new sens for {game_convert} is: {new_sens}")
        



# something went wrong
else :
    print(f"{game} is not supported or typed wrong try to type again.\n")