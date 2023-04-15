"""Animals"""
class Animal:
    """Animal"""
    def __init__(self, name):
        self._name = name
        self.species = None

class Mammal(Animal):
    """Mammal"""
    def __init__(self, name):
        super().__init__(name)
        self.num_legs = None

class Dog(Mammal):
    """Dog"""
    def __init__(self, name, breed):
        super().__init__(name)
        self._breed = breed
        self.species = 'Canis lupus familiaris'
        self.num_legs = 4
    @staticmethod
    def make_sound():
        """Make a sound"""
        return 'Woof!'
    @property
    def breed(self):
        """breed"""
        return self._breed
    @breed.setter
    def breed(self, value):
        if isinstance(value, str):
            self._breed = value
        else:
            raise TypeError("Breed must be a string")

class Cat(Mammal):
    """Cat"""
    def __init__(self, name, color):
        super().__init__(name)
        self._color = color
        self.species = 'Felis catus'
        self.num_legs = 4
    @staticmethod
    def make_sound():
        """Make a sound"""
        return 'Meow!'
    @property
    def color(self):
        """Cat"""
        return self._color
    @color.setter
    def color(self, value):
        if isinstance(value, str):
            self._color = value
        else:
            raise TypeError("Color must be a string")

class FlyingAnimal:
    """Flying Animal"""
    def __init__(self, name):
        self._name=name
        self._wingspan = 0
    @property
    def wingspan(self):
        """wingspan"""
        return self._wingspan
    @wingspan.setter
    def wingspan(self, value):
        if isinstance(value, int):
            self._wingspan = value
        else:
            raise TypeError("Wingspan must be an integer")

class Bird(FlyingAnimal):
    """Bird"""
    def __init__(self, name):
        super().__init__(name)
        self.species=None
    @staticmethod
    def make_sound():
        """Make a sound"""
        return 'Chirp!'

class Parrot(FlyingAnimal):
    """Parrot"""
    def __init__(self, name, language):
        super().__init__(name)
        self._language = language
        self._wingspan = 20
        self.species = 'Psittaciformes'
    @staticmethod
    def make_sound():
        """Make a sound"""
        return 'Polly wants a cracker!'
