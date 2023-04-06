"""A class used to test animals Class"""
from animals import Animal, Mammal, Dog, Cat, Bird, FlyingAnimal, Parrot

def test_Animals():
    """
    Print Done if all tests passed
    """
    print("Testing Animals class...")
    # Test Animal class
    animal = Animal('generic')
    assert animal.species == None
    assert animal._name == 'generic'
    animal1 = Animal('abstract')
    assert animal1 != animal
    assert isinstance(animal, Animal)
    try:
    # create an animal with a non-string name
        animal = Animal(123)
    except TypeError:
    # this will be executed if a TypeError is raised
        pass

    # Test Mammal class
    mammal = Mammal('generic')
    assert mammal.species == None
    assert mammal._name == 'generic'
    assert mammal.num_legs == None
    assert isinstance(mammal, Mammal)
    assert isinstance(mammal, Animal)

    # Test Dog class
    dog = Dog('Fido', 'Golden Retriever')
    assert dog.species == 'Canis lupus familiaris'
    assert dog._name == 'Fido'
    assert dog._breed == 'Golden Retriever'
    assert dog.num_legs == 4
    assert dog.make_sound() == 'Woof!'
    dog._breed = 'Labrador'
    assert dog.breed == 'Labrador'
    try:
        dog._breed = 123
    except TypeError:
        pass
    assert isinstance(dog, Dog)
    assert isinstance(dog, Mammal)
    assert isinstance(dog, Animal)

    #Test FlyingAnimal class
    flying_animal = FlyingAnimal('generic')
    assert flying_animal._name == 'generic'
    assert flying_animal._wingspan == 0
    flying_animal._wingspan = 10
    assert flying_animal._wingspan == 10
    try:
        flying_animal._wingspan = '10'
    except TypeError:
        pass
    # Test Cat class
    cat = Cat('Whiskers', 'Grey')
    assert cat.species == 'Felis catus'
    assert cat._name == 'Whiskers'
    assert cat._color == 'Grey'
    assert cat.num_legs == 4
    assert cat.make_sound() == "Meow!"
    assert isinstance(cat, Cat)
    assert isinstance(cat, Mammal)
    assert isinstance(cat, Animal)
    my_cat = Cat("Fluffy", 3)
    my_cat.name = "Mittens"
    my_cat.age = 5
    assert my_cat.name == "Mittens"
    assert my_cat.age == 5
    try:
        my_cat.age = '5'
    except AssertionError:
        pass

    # Test Bird class
    bird = Bird('generic')
    assert bird.species is None
    assert bird._name == 'generic'
    assert bird.make_sound() == 'Chirp!'
    assert bird.wingspan == 0 # default value

    # Test Parrot class
    parrot = Parrot('Polly', 'English')
    assert parrot.species == 'Psittaciformes'
    assert parrot._name == 'Polly'
    assert parrot._language == 'English'
    assert parrot.wingspan == 20
    assert parrot.make_sound() == 'Polly wants a cracker!'

    print('Done!')


if __name__ == '__main__':
    test_Animals()
