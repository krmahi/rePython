import sys
import random
import os

class Animal: 
    __name = "" # this class is not initialized by itself
    __height = 0
    __weight = 0
    __sound = ""

    def __init__(self, name, height, weight, sound):
        self.__name = name 
        self.__height = height 
        self.__weight = weight
        self.__sound = sound
        
    # we can initialize set and get functions for every attribute

    def set_name(self, name: (str)) -> str: # to show how to define types
        self.__name = name

    def set_height(self, height: (int)) -> int: # to show how to define types
        self.__height = height

    def set_weight(self, weight: (int)) -> int: # to show how to define types
        self.__weight = weight

    def set_sound(self, sound: (str)) -> str: # to show how to define types
        self.__sound= sound
    
    def get_name(self):
        return self.__name
    
    def get_height(self):
        return self.__height
    
    def get_weight(self):
        return self.__weight
    
    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal") # just to print the class name

    def getinstring(self):
        return "{} is {}cm tall and {}kg and say {}".format(self.__name, 
                                                            self.__height,
                                                            self.__weight,
                                                            self.__sound) # another way beside c operator 

# obj1 = Animal("mahi1", 12, 22, 1)
# obj1.set_name("mahi")
# animal_name = obj1.get_name()
# print(animal_name) # mahi
# or
# print(obj1._Animal__name) # mahi

cat = Animal("wiskers", 22, 10, 'meow') # obj creation
animal = cat.getinstring()
print(animal)

# python Class name mangling

class myClass:
    # def __init__(self, name, height, weight, sound): this is a constructor to construct an object
    def __init__(self): # this is a initializer not a constructor (since it does not have arguments mor elike static)
        self.__name = "mahi" # can also be written as -> __name = "mahi"
    
    def display_name(self):
        print(self.__name)

obj = myClass()
obj.display_name() # prints mahi

# Python name mangling

print(obj._myClass__name) # prints mahi


# *** INHERITENCE ***
# (inherit variables, attributes, functions from parrent class)

class pets(Animal): # every pet is an animal, but not all animals are pet
    __owner = ""

    def __init__(self, name, height, weight, sound, owner): # this can have attributes from the parent class
        super().__init__(name, height, weight, sound )
        self.__owner = owner

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner
    
    def get_type(self):
        print("Pets")

    #overwriting a function in super(parrent) class

    def getinstring(self):
        # return super().getinstring()
        return "{} is {}cm tall and {}kg and say {} and his owner is {}".format(self._Animal__name, 
                                                            self._Animal__height,
                                                            self._Animal__weight,
                                                            self._Animal__sound,
                                                            self.__owner) # either use mangling or get functions
         
     

obj2 = pets("neko", 21, 9, 'meoww', 'mahi')
Pet_animal = obj2.getinstring()
print(Pet_animal)