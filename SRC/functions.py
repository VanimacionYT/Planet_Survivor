from SRC.options import *
from SRC.Control.Global import GlobalState
from SRC.variables import *
from SRC.hints import *
from SRC.options import *
import os, time
import getpass as gp
from termcolor import *

#--- GENERAL FUNCTIONS ---#

#Returns desired text in format
def custom_envirorment_dificulty_text(dificulty: custom_envirorment_dificulty_hints) -> str:
    """Custom function that returns specified text's back with color formatting"""
    try:
        format_dificulty = dificulty.lower()
        if format_dificulty == "easy":
            return colored(dificulty, color="green", on_color="on_black")
        elif format_dificulty == "hard":
            return colored(dificulty, color="yellow", on_color="on_black")
        elif format_dificulty == "hostile":
            return colored(dificulty, color="red", on_color="on_black")
        else:
            raise ValueError
    except:
        return dificulty

#Returns desired text in format
def custom_material_level_text(material_level: custom_material_level_hints) -> str:
    """Custom function that returns specified text's back with color formatting"""
    try:
        format_dificulty = material_level.lower()
        if format_dificulty == "common":
            return colored(material_level, color="green", on_color="on_black")
        elif format_dificulty == "rare":
            return colored(material_level, color="yellow", on_color="on_black")
        elif format_dificulty == "scarce":
            return colored(material_level, color="red", on_color="on_black")
        else:
            raise ValueError
    except:
        return material_level
    
#Returns desired text in format
def custom_conection_speed_text(conections_speed: custom_conection_speed_hints) -> str:
    """Custom function that returns specified text's back with color formatting"""
    try:
        format_dificulty = conections_speed.lower()
        if format_dificulty == "fast":
            return colored(conections_speed, color="green", on_color="on_black")
        elif format_dificulty == "slow":
            return colored(conections_speed, color="yellow", on_color="on_black")
        elif format_dificulty == "very slow":
            return colored(conections_speed, color="red", on_color="on_black")
        else:
            raise ValueError
    except:
        return conections_speed

#Function that returns the input text "option" in the desired format
def custom_selections_bar_text(option):
    return colored(option, "light_green", "on_black")

#Function that clears the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#The top line that always will apear on every print
def top_info_line():
    OptionsControler = Options()
    OptionsControler.OptionsLoader()
    clear_screen()
    print(colored(f"Planet Survivor______________________________________________________________________________________________________{GlobalState.Version}", OptionsControler.GetTopInfoLineColor(), "on_black") + colored("\n"))

#The functions asks the player if he really wants to leave the game
def ask_exit():
    while True:
        clear_screen()
        top_info_line()
        print(colored("Do you really wanna quit?", color="yellow", on_color="on_black"), colored("\nAny unsaved data may be lost.\n", color="white", on_color="on_black"), colored("\n1 - Yes", color="yellow", on_color="on_black"), "     ", colored("2 - No", color="yellow", on_color="on_black"))
        option = gp.getpass("")
        if option == "1":
            exit(0)
        elif option == "2":
            break
        else:
            print("Bad Option!")
            time.sleep(2)

#--- GAME CREATION ---#

#The function prints the planets to choose
"""WIP to Automate"""
def print_select_planet() -> str:
    #WIP AUTOMATE TABLE FORMATTING BASED ON OLANET NAME LENGHT
    print(f"\t", colored("1  |  ",color="yellow"), f"Borealis\t[Envirorment - {custom_envirorment_dificulty_text("Easy")}]\t   [Materials & Food - {custom_material_level_text("Common")}]\t   [Conection Speed - {custom_conection_speed_text("Fast")}]")
    print(f"\t", colored("2  |  ",color="yellow"), f"Trappis\t\t[Envirorment - {custom_envirorment_dificulty_text("Hard")}]\t   [Materials & Food - {custom_material_level_text("Rare")}]\t   [Conection Speed - {custom_conection_speed_text("Slow")}]")
    print(f"\t", colored("3  |  ",color="yellow"), f"Kamma\t\t[Envirorment - {custom_envirorment_dificulty_text("Hostile")}]\t   [Materials & Food - {custom_material_level_text("Scarce")}]\t   [Conection Speed - {custom_conection_speed_text("Very Slow")}]")        