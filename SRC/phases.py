import time
import termcolor as tc
import getpass as gp
from SRC.functions import *
from SRC.variables import *
from SRC.options import *
from SRC.Control.Current import CurrentState
from SRC.Control.Global import GlobalState

#File that manages the diverse files

def TITLE():
    clear_screen()
    #Short animation for the title
    for x in range(len(striped_title)):
        line=tc.colored(striped_title[x], color=title_colors[x])
        print(line)
        time.sleep(0.1)
    gp.getpass("\nPress 'Enter' to continue")
    #Loads and initiates Options
    OptionsControler = Options()
    OptionsControler.OptionsLoader()
    #Goes to Menu
    GlobalState.GlobalGame = CurrentState.MENU

def MENU():
    menu = True
    #While loop to mantain the menu screen
    while menu == True:
        top_info_line()
        for x in range(len(striped_title)):
            line=tc.colored(striped_title[x], color=title_colors[x])
            print(line)
        print("\n", colored(f"--- Main Menú ---", color="red", on_color="on_black"), "\n\n", colored("\t1  |", "yellow"), "  Create New Game\n", colored("\t2  |", "yellow"), "  Load Saved Game\n", colored("\t3  |", "yellow"), "  Check Milestones\n", colored("\t4  |", "yellow"), "  Options\n", colored("\t5  |", "yellow"), "  Exit\n")
        selection = gp.getpass("")
        
        #Create new game
        if selection == "1":
            GlobalState.GlobalGame = CurrentState.CREATE_GAME_MENU
            break
        #Load saved game
        elif selection == "2":
            GlobalState.GlobalGame = CurrentState.LOAD_GAME_MENU
            break
        #Check milestiones
        elif selection == "3":
            GlobalState.GlobalGame = CurrentState.CHECK_MILESTONES_MENU
            break
        #Options
        elif selection == "4":
            GlobalState.GlobalGame = CurrentState.OPTIONS_MENU
            break
        #Exit
        elif selection == "5":
            ask_exit()

def CREATE_GAME_MENU():
    pass

###Must add a continue option (last save)
def LOAD_GAME_MENU():
    pass

def CHECK_MILESTONES_MENU():
    pass

def OPTIONS_MENU():
    while True:
        top_info_line()
        for x in range(len(striped_title)):
            line=tc.colored(striped_title[x], color=title_colors[x])
            print(line)
        print("\n", colored(f"--- Options ---", color="red", on_color="on_black"), "\n\n", colored("\t1  |", "yellow"), "  Change Top Line Color\n", colored("\t2  |", "yellow"), "  Back to Main Menu\n")
        selection = gp.getpass("")

        #Change top line color
        if selection == "1":
            top_info_line()
            print("\nSelect a color for the top line info text:\n", colored("\t1  | Red (Default)\n", color="red", on_color="on_black"), colored("\t2  | Green\n", color="green", on_color="on_black"), colored("\t3  | Yellow\n", color="yellow", on_color="on_black"), colored("\t4  | Blue\n", color="blue", on_color="on_black"), colored("\t5  | Magenta\n", color="magenta", on_color="on_black"), colored("\t6  | Cyan\n", color="cyan", on_color="on_black"), colored("\t7  | White\n", color="white", on_color="on_black"))
            option = gp.getpass("")
            if option == "1":
                color="red"
            elif option == "2":
                color="green"
            elif option == "3":
                color="yellow"
            elif option == "4":
                color="blue"
            elif option == "5":
                color="magenta"
            elif option == "6":
                color="cyan"
            elif option == "7":
                color="white"
            else:
                top_info_line()
                print("Wrong Value! Try Again")
            Options.ChangeTopInfoLineColor(Options, color)
        #Exit
        elif selection == "2":
            GlobalState.GlobalGame = CurrentState.MENU
            break