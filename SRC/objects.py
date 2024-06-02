#This file stores all objects in the project

import random
from SRC.variables import mnames_route,fnames_route,surnames_route

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
        #Asigns rng range values depending on the level
        if self.__level == "Normal":
            self.__rng = random.randint(30,40)
        elif self.__level == "WellTrained":
            self.__rng = random.randint(20,30)
        elif self.__level == "Tryhard":
            self.__rng == random.randint(10,20)

        #Randomly Selects NPC genere and asigns name
        self.__genere_ID = random.randint(1, 2)
        if self.__genere_ID == 1:
            self.__genere = "Male"
            with open(mnames_route, 'r', encoding="utf8") as mnames:
                mnames.seek(0)
                name = 1-random.randint(1,(len(mnames.readlines())))
                mnames.seek(0)
                lines = mnames.read()
                lines = lines.split("\n")
                name = (lines[name])
                mnames.close
            self.__name = name
        else:
            self.__genere = "Female"
            with open(fnames_route, 'r', encoding="utf8") as fnames:
                fnames.seek(0)
                name = 1-random.randint(1,(len(fnames.readlines())))
                fnames.seek(0)
                lines = fnames.read()
                lines = lines.split("\n")
                name = (lines[name])
                fnames.close
            self.__name = name
        
        #asigns surnames
        with open(surnames_route, 'r', encoding="utf8") as surnames:
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

    #Getters
    @property
    def genere(self):
        return self.__genre
    @property
    def name(self):
        return self.__name
    @property
    def surame(self):
        return self.__surname
    @property
    def hunger(self):
        return self.__hunger
    @property
    def is_hungry(self):
        return self.__is_hungry
    @property
    def level(self):
        return self.__level
    @property
    def rng(self):
        return self.__rng
    @property
    def is_alive(self):
        return self.__is_alive

    #Setters
    @genere.setter
    def genere(self, new):
        self.__genre = new
    @name.setter
    def name(self, new):
        self.__name = new
    @surame.setter
    def surame(self, new):
        self.__surname = new
    @hunger.setter
    def hunger(self, new):
        self.__hunger = new
    @is_hungry.setter
    def is_hungry(self, new):
        self.__is_hungry = new
    @level.setter
    def level(self, new):
        self.__level = new
    @rng.setter
    def rng(self, new):
        self.__rng = new
    @is_alive.setter
    def is_alive(self, new):
        self.__is_alive = new

class Planet():
    __envirorment_rng = 0
    __food_rng = 0
    __materials_rng = 0
    __conection_speed = 0
    __planet_name = ""

    def __init__(self, envirorment_rng, food_rng, materials_rng, conection_speed, planet_name):
        self.__envirorment_rng = envirorment_rng
        self.__food_rng = food_rng
        self.__materials_rng = materials_rng
        self.__conection_speed = conection_speed
        self.__planet_name = planet_name

class Base():
    __base_name = ""
    __materials_storage = 0
    __food_storage = 0
    __antena_status = 0
    __message_status = 0
    __crew_members = []
    __injured_crew_members = []
    __healthy_crew_members = []

    def __init__(self, base_name, materials_storage, food_storage, crew_members):
        self.__base_name = base_name
        self.__materials_storage = materials_storage
        self.__food_storage = food_storage
        self.__crew_members = crew_members
        self.__antena_status = 100
        self.__message_status = 0
        self.__healthy_crew_members = self.__crew_members

class Company():
    def __init__(self, company_name, materials, food, base_strength):
        pass