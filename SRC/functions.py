from SRC.options import *
from SRC.Control.Global import GlobalState
from SRC.variables import *
from SRC.options import *
import os, time
import getpass as gp
from termcolor import *

#--- GENERAL FUNCTIONS ---#
#Function that returns the input text "options" in the desired format
def options_bar(options):
    return colored(f"{options}", "light_green", "on_black")

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