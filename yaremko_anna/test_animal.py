import unittest
from animal import Animal, Mammal, Dog, Cat, FlyingAnimal, Bird, Parrot

class AnimalTest(unittest.TestCase):

    def test_animal(self):
        with self.assertRaises(TypeError):
            Animal(1)
        self.assertIsNone(Mammal.num_legs)

    def test_dog(self):
        with self.assertRaises(TypeError):
            Dog(999, 'Labrador') 
        dog = Dog('Bars', 'Labrador')
        self.assertEqual(dog.breed, 'Labrador')
        self.assertEqual(Dog.num_legs, 4)
        self.assertEqual(Dog.species, 'Canis lupus familiaris')
        dog = Dog('Bars', 'Labrador')
        self.assertEqual(dog.make_sound(), 'Woof!')

    def test_flying_animal(self):
        with self.assertRaises(TypeError):
            FlyingAnimal(123)
        flying_animal = FlyingAnimal('Crow')
        self.assertEqual(flying_animal.wingspan, 0)

    def test_cat(self):
        self.assertEqual(Cat.num_legs, 4)
        self.assertEqual(Cat.species, 'Felis catus')
        cat = Cat('Murka', 'Red')
        self.assertEqual(cat.make_sound(), 'Meow!')

    def test_bird(self):
        bird = Bird('Crow')
        self.assertEqual(bird.make_sound(), 'Chirp!')

    def test_parrot(self):
        self.assertEqual(Parrot.wingspan, 20)
        self.assertEqual(Parrot.species, 'Psittaciformes')
        parrot = Parrot('Dolly', 'French')
        self.assertEqual(parrot.make_sound(), 'Dolly wants a cracker!')


if __name__ == '__main__':
    unittest.main()