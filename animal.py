class Animal:
    def __init__(self, name: str, species:str, age:int, adopted:bool):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__adopted = adopted

    def get_name(self):
        return self.__name
    
    def set_name(self, New_name):
        self.__name = New_name

    def get_species(self):
        return self.__species

    def set_species(self, New_species):
        self.__species = New_species
    
    def get_age(self):
        return self.__age

    def set_age(self, New_age):
        self.__age = New_age

    def get_adopted(self,):
        return self.__adopted

    def set_adopted(self, New_adopted):
        self.__adopted = New_adopted
    
    def Make_sound(noise):
        return "This animal makes a sound"


class Dog(Animal):
    def __init__(self, name: str, species:str, age:int, breed:str, adopted:bool):
        super().__init__(name, species, age, adopted)
        self.__breed = breed 
    
    def get_breed(self):
        return self.__breed
    
    def set_breed(self, new_breed):
        self.__breed = new_breed
    
    def Make_sound(noise):
        return "Woof!"
    

class Cat(Animal):
    def __init__(self, name: str, species:str, age:int, indoor_only:bool, adopted:bool):
        super().__init__(name, species, age, adopted)
        self.__indoor = indoor_only

    def get_indoor_only(self):
        return self.__indoor
    
    def set_indoor_only(self, new_indoor):
        self.__indoor = new_indoor

    def Make_sound(noise):
        return "Meow!"



