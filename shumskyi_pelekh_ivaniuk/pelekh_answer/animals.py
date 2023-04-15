"""
classes for Anya Syvkova's asserts
"""
class Animal:
    """A base class representing an animal."""
    species = None
    def __init__(self, name: str) -> None:
        """Constructs an instance of the Animal class with a given name."""
        self._name = name


class Mammal(Animal):
    """A subclass of Animal representing a mammal."""
    num_legs = None


class Dog(Mammal):
    """A subclass of Mammal representing a dog."""
    species = 'Canis lupus familiaris'
    num_legs = 4
    def __init__(self, name: str, breed: str) -> None:
        """Constructs an instance of the Dog class with a given name and breed."""
        super().__init__(name)
        self._breed = breed

    def make_sound(self):
        """Returns a string representing the sound a dog makes."""
        return 'Woof!'

    @property
    def breed(self):
        """Returns the breed of the dog."""
        return self._breed


class Cat(Mammal):
    """A subclass of Mammal representing a cat."""
    species = 'Felis catus'
    num_legs = 4
    def __init__(self, name: str, color: str) -> None:
        """Constructs an instance of the Cat class with a given name and color."""
        super().__init__(name)
        self._color = color

    def make_sound(self):
        """Returns a string representing the sound a cat makes."""
        return "Meow!"


class FlyingAnimal(Animal):
    """A base class representing a flying animal."""
    _wingspan = 0
    @property
    def wingspan(self):
        """Returns the wingspan of the flying animal."""
        return self._wingspan


class Bird(FlyingAnimal):
    """A subclass of FlyingAnimal representing a bird."""
    def make_sound(self):
        """Returns a string representing the sound a bird makes."""
        return 'Chirp!'


class Parrot(Bird):
    """A subclass of Bird representing a parrot."""
    _wingspan = 20
    species = 'Psittaciformes'
    def __init__(self, name: str, language: str) -> None:
        """Constructs an instance of the Parrot class with a given name and language."""
        super().__init__(name)
        self._language = language

    def make_sound(self):
        """Returns a string representing the sound a parrot makes."""
        return 'Polly wants a cracker!'
