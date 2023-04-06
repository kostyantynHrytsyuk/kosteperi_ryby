"""Animals module"""
class Animal:
    """Base class for all animals"""
    species = None
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self._name = name

class Mammal(Animal):
    """Base class for all mammals"""
    num_legs = None

    def __init__(self, name):
        super().__init__(name)


class FlyingAnimal:
    """Base class for all flying animals"""
    _wingspan = 0

    def __init__(self, name):
        self._name = name

    @property
    def wingspan(self):
        """Wingspan of the bird"""
        if not isinstance(self._wingspan, int):
            raise TypeError("Wingspan must be an integer")
        return self._wingspan


class Dog(Mammal):
    """A dog"""
    species = 'Canis lupus familiaris'
    num_legs = 4

    def __init__(self, name, breed):
        super().__init__(name)
        self._breed = breed

    @property
    def breed(self):
        """Breed of the dog"""
        if not isinstance(self._breed, str):
            raise TypeError("Breed must be a string")
        return self._breed

    @staticmethod
    def make_sound():
        """Make a sound"""
        return "Woof!"


class Cat(Mammal):
    """A cat"""
    species = 'Felis catus'
    num_legs = 4

    def __init__(self, name, color, age=1):
        super().__init__(name)
        self._color = color
        self._age = age

    def color(self):
        """Color of the cat"""
        return self._color

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        assert isinstance(value, str), "Name must be a string"
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        assert isinstance(value, int) and value > 0, "Age must be a positive integer"
        self._age = value

    @staticmethod
    def make_sound():
        """Make a sound"""
        return "Meow!"


class Bird(Animal, FlyingAnimal):
    """Base class for all birds"""
    species = None

    def __init__(self, name):
        Animal.__init__(self, name)
        FlyingAnimal.__init__(self, name)

    @staticmethod
    def make_sound():
        """Make a sound"""
        return "Chirp!"


class Parrot(Bird):
    """A parrot"""
    wingspan = 20
    species = 'Psittaciformes'

    def __init__(self, name, language):
        super().__init__(name)
        self._language = language

    def language(self):
        """Language of the parrot"""
        return self._language

    @staticmethod
    def make_sound():
        """Make a sound"""
        return "Polly wants a cracker!"
