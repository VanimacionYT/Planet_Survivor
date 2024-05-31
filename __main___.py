#################################
#       Importing Area          #
#################################
from SRC.phases import *
from SRC.Control.Global import GlobalState
from SRC.Control.Current import CurrentState

while True:
    if GlobalState.GlobalGame == CurrentState.TITLE:
        TITLE()
    elif GlobalState.GlobalGame == CurrentState.MENU:
        MENU()
    elif GlobalState.GlobalGame == CurrentState.CREATE_GAME_MENU:
        CREATE_GAME_MENU()
    elif GlobalState.GlobalGame == CurrentState.LOAD_GAME_MENU:
        LOAD_GAME_MENU()
    elif GlobalState.GlobalGame == CurrentState.CHECK_MILESTONES_MENU:
        CHECK_MILESTONES_MENU()
    elif GlobalState.GlobalGame == CurrentState.OPTIONS_MENU:
        OPTIONS_MENU()