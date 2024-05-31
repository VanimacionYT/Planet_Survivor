import random
from SRC.variables import mnames_route,fnames_route,surnames_route
#File saves all objects
class NPC():
    __genere = ""
    __name = ""
    __surname = ""
    __hunger = ""
    __is_hungry = False
    __level = ""
    __rng = 0
    __is_alive = False


    def __init__(self, level):
        self.__is_alive = True
        self.__level = level
        if self.__level == "Normal":
            self.__rng = random.randint(30,40)
        elif self.__level == "WellTrained":
            self.__rng = random.randint(20,30)
        elif self.__level == "Tryhard":
            self.__rng == random.randint(10,20)
        self.__genere_ID = random.randint(1, 2)
        if self.__genere_ID == 1:
            self.__genere = "Male"
            with open(mnames_route, 'r') as mnames:
                mnames.seek(0)
                name = 1-(random.randint(1,(len(mnames.readlines()))))
                mnames.seek(0)
                lines = mnames.read()
                lines = lines.split("\n")
                name = (lines[name])
                mnames.close
            self.__name = name
        else:
            self.__genere = "Female"
            with open(fnames_route, 'r') as fnames:
                fnames.seek(0)
                name = 1-random.randint(1,(len(fnames.readlines())))
                fnames.seek(0)
                lines = fnames.read()
                lines = lines.split("\n")
                name = (lines[name])
                fnames.close
            self.__name = name
        with open(surnames_route, 'r') as surnames:
            surnames.seek(0)
            surname = 1-random.randint(1,(len(surnames.readlines())))
            surnames.seek(0)
            lines = surnames.read()
            lines = lines.split("\n")
            surname = (lines[surname])
            surnames.close
        self.__surname = surname
        self.__hunger = 100
        self.__is_hungry = False

    def __str__(self):
        return f"CREW MEMBER\n\tName: {self.__name} {self.__surname} ({self.__genere})\n\tLevel: {self.__level}\n\tRNG: {self.__rng}\n\tHunger: {self.__hunger}\n\tState: {self.__is_alive}"

    #eat makes the npc consume materials to eat (1 material = +30/60 hunger)
    def eat():
        pass
    #check_hunger is activated every day and if an NPC has >20 hunger it tries to eat
    def check_hunger(self):
        if self.__hunger <= 20:
            self.eat()

class Planet():
    __envirorment_rng = 0
    __food_rng = 0
    __materials_rng = 0
    __conection_speed = 0
    __planet_name = ""

    def __init__(self, envirorment_rng, food_rng, materials_rng, conections_rng, planet_name)