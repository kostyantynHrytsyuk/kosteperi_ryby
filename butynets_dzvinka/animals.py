class Animal:

    species = None

    def __init__(self, name: str) -> None:
        """
        Initialize class Animal
        """
        self._name = Animal.check_correct(name)

    def __eq__(self, __value: object) -> bool:
        """
        Comparing two objects
        """
        return self.__dict__ == __value.__dict__
    
    @staticmethod
    def check_correct(name:str):
        """
        Checing name
        """
        if not isinstance(name, str):
            raise TypeError("Incorrect name!")
        else:
            return name

class Mammal(Animal):

    num_legs = None
    def __init__(self, name: str) -> None:
        super().__init__(name)
        
    
class Dog(Mammal):

    species = 'Canis lupus familiaris'
    num_legs = 4
    def __init__(self, name: str, breed:str) -> None:
        super().__init__(name)
        self._breed = breed

    @staticmethod
    def make_sound():
        """
        Make sound
        """
        return 'Woof!'
    
    @property
    def breed(self):
        if isinstance(self._breed, str):
            return self._breed
        else:
            raise TypeError("Breed is not correct!")
    
class FlyingAnimal(Animal):

    def __init__(self, name: str, wing=0) -> None:
        super().__init__(name)
        self._wingspan = FlyingAnimal.check_correct(wing)
    
    @staticmethod
    def check_correct(wing:int):
        if isinstance(wing, int):
            return wing
        else:
            raise TypeError("Incorrect wing!")

class Cat(Mammal):

    num_legs = 4
    species = 'Felis catus'

    def __init__(self, name: str, color:str, age = 0) -> None:
        super().__init__(name)
        self._color = color
        self.age = Cat.check_correct(age)

    @staticmethod
    def make_sound():
        """
        Make sound
        """
        return "Meow!"
    
    @staticmethod
    def check_correct(age:str):
        """
        Checing name
        """
        if not isinstance(age, int):
            raise AssertionError("Incorrect age!")
        else:
            return age   

class Bird(FlyingAnimal):

    def __init__(self, name: str, wing=0) -> None:
        super().__init__(name, wing)
        self.__wingspan = 0

    @staticmethod
    def make_sound():
        """
        Make sound
        """
        return 'Chirp!'
    
    @property
    def wingspan(self):
        return self.__wingspan
    
class Parrot(Bird):

    species = 'Psittaciformes'

    def __init__(self, name: str, lang:str, wing=20) -> None:
        super().__init__(name, wing)
        self.__wingspan = wing
        self._language = lang

    @property
    def wingspan(self):
        return self.__wingspan
    
    @staticmethod
    def make_sound():
        """
        Make sound
        """
        return 'Polly wants a cracker!'
