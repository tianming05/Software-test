from random import choice

NAME_DB_FILE = "names.txt" # File containing names, one per line

class Hello:
    """A simple class for generating a hello world string."""
    
    def __init__(self, name = "World"):
        self.name = name
        with open(NAME_DB_FILE) as namedb:
            self.__name_list = namedb.readlines()
            self.__name_list = [name.strip() for name in self.__name_list]

    @property
    def name(self):
        return self.__name

    def name_list(self):
        return self.__name_list

    @name.setter
    def name(self, value):
        self.__name = str(value)

    def add(self, name):
        self.__name_list = [name,]

    def pick_random(self):
        self.name = choice(self.__name_list)

    def __str__(self):
        if len(self.name) == 0:
            return "Hello!"
        else:
            return "Hello, {}!".format(self.name)
