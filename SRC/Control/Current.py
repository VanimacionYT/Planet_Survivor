from enum import Enum

class CurrentState(Enum):
    TITLE = 0
    MENU = 1
    CREATE_GAME_MENU = 2
    LOAD_GAME_MENU = 3
    CHECK_MILESTONES_MENU = 4
    OPTIONS_MENU = 5