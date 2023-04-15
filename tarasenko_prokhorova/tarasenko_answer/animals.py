"""animals implementation"""
class Animal:
    """main animal class"""
    def __init__(self, name, species = None, sound = None):
        self._name = name
        self.species = species
        self.sound = sound
        if not isinstance(self._name, str):
            raise TypeError
    def make_sound(self):
        """make sound method"""
        return f'{self.sound}'

class Mammal(Animal):
    """mammal class"""
    def __init__(self, name, species = None, num_legs = None):
        self._name = name
        self.species = species
        self.num_legs = num_legs

class Dog(Mammal):
    """dog class"""
    species = 'Canis lupus familiaris'
    sound = 'Woof!'
    def __init__(self, name, breed, num_legs = 4):
        self._name = name
        self._breed = breed
        self.num_legs = num_legs

    @property
    def breed(self):
        """getter for breed property"""
        return self._breed

    @breed.setter
    def breed(self, new_breed):
        """setter for breed property"""
        self._breed = new_breed

class FlyingAnimal(Animal):
    """flying animal class"""
    def __init__(self, name, wingspan = 0):
        self._name = name
        self.wingspan = wingspan
    @property
    def wingspan(self):
        """getter for wingspan property"""
        return self._wingspan
    @wingspan.setter
    def wingspan(self, new_wingspan):
        """setter for wingspan property"""
        self._wingspan = new_wingspan

class Cat(Mammal):
    """cat class"""
    species = 'Felis catus'
    sound = 'Meow!'
    def __init__ (self, name, color, num_legs = 4):
        self._name = name
        self._color = color
        self.num_legs = num_legs

class Bird(FlyingAnimal):
    """bird class"""
    species = None
    sound = 'Chirp!'
    def __init__ (self, name):
        super().__init__(name, 0)

class Parrot(FlyingAnimal):
    """parrot class"""
    species = 'Psittaciformes'
    sound = 'Polly wants a cracker!'
    def __init__ (self, name, language, ):
        super().__init__(name, 20)
        self._language = language
