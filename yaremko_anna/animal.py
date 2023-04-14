class Animal:
    def __init__(self, name):
        self._name=name
        if not isinstance(name,str):
            raise TypeError
        Animal.species = None

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
    num_legs=None

class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name) 
        self._breed=breed
        Dog.num_legs=4
        Dog.species = 'Canis lupus familiaris'

    @property
    def breed(self):
        if not isinstance(self._breed, str):
            raise TypeError
        else:
            return self._breed
        
    def make_sound(self):
        return 'Woof!'

class FlyingAnimal(Animal):
    def __init__(self, name):
        super().__init__(name) 
        FlyingAnimal._wingspan=0

    @property
    def wingspan(self):
        if not isinstance(self._wingspan, int):
            raise TypeError
        else:
            return self._wingspan
        
class Cat(Mammal):
    def __init__(self, name, color):
        super().__init__(name) 
        self._color=color
    species='Felis catus'
    num_legs=4

    def make_sound(self):
        return 'Meow!'

class Bird(FlyingAnimal):
    def __init__(self, name):
        super().__init__(name) 

    def make_sound(self):
        return 'Chirp!'

class Parrot(Bird):
    species = 'Psittaciformes'
    wingspan=20
    def __init__(self, name, language):
        super().__init__(name)
        self._language=language

    def make_sound(self):
        return f'{self._name} wants a cracker!'