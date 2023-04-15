import unittest
from animals_tarasenko import *

class Test(unittest.TestCase):

    def test_animal(self):
        self.assertRaises(TypeError, lambda: Animal(123, 'cat', 'Meow!'))
        animal = Animal('Bob', 'dog', 'Woof!')
        self.assertEqual(animal.make_sound(), 'Woof!')
    def test_dog(self):
        dog = Dog('Fido', 'Labrador Retriever')
        self.assertEqual(dog.breed, 'Labrador Retriever')
        dog.breed = 'Golden Retriever'
        self.assertEqual(dog.breed, 'Golden Retriever')
        dog = Dog('Buddy', 'Golden Retriever')
        self.assertEqual(dog.breed, 'Golden Retriever')
        dog.breed = 'Labrador Retriever'
        self.assertEqual(dog.breed, 'Labrador Retriever')

    def test_mammal(self):
        mammal = Mammal('Bob', 'dog')
        self.assertEqual(mammal.num_legs, None)
        mammal = Mammal('Bob', 'dog', num_legs=3)
        self.assertEqual(mammal.num_legs, 3)

    def test_cat(self):
        cat = Cat('Whiskers', 'Gray')
        self.assertEqual(cat.species, 'Felis catus')
        cat = Cat('Whiskers', 'Gray')
        self.assertEqual(cat.num_legs, 4)
        cat = Cat('Whiskers', 'Gray', num_legs=3)
        self.assertEqual(cat.num_legs, 3)
        cat = Cat('Whiskers', 'Gray')
        self.assertEqual(cat.make_sound(), 'Meow!')

    def test_wingspan(self):
        flying_animal = FlyingAnimal('Birdie')
        self.assertEqual(flying_animal.wingspan, 0)
        flying_animal.wingspan = 10
        self.assertEqual(flying_animal.wingspan, 10)

    def test_make_sound(self):
        bird = Bird('Tweety')
        self.assertEqual(bird.make_sound(), 'Chirp!')

    def test_parrot(self):
        parrot = Parrot('Polly', 'English')
        self.assertEqual(parrot._language, 'English')
        parrot._language = 'Spanish'
        self.assertEqual(parrot._language, 'Spanish')
        parrot = Parrot('Polly', 'English')
        self.assertEqual(parrot.wingspan, 20)
        parrot = Parrot('Polly', 'English')
        self.assertEqual(parrot.make_sound(), 'Polly wants a cracker!')


if __name__ == '__main__':
    unittest.main()
