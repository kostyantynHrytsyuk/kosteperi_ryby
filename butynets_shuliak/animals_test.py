import unittest
from animals import Animal, Parrot, Bird, FlyingAnimal, Cat, Dog, Mammal

class TestAnimal(unittest.TestCase):
    """
    Testing animals module
    """
    def test_dog(self):
        """
        Testing class Dog
        """
        animal1 = Animal("max")
        animal2 = Animal("dina")
    
        dog = Dog('Fido', 'Golden Retriever')
        self.assertEqual(dog.breed, 'Golden Retriever')
        self.assertEqual(dog.num_legs, 4)
        self.assertEqual(dog.make_sound(), 'Woof!')
        self.assertEqual(dog._name, 'Fido')
        self.assertIsInstance(dog, Animal)
        self.assertIsInstance(dog, Mammal)
        self.assertFalse(animal1.__eq__(animal2), False)

        self.assertRaises(TypeError, dog.check_correct, 12)

    def test_cat(self):
        """
        Testing class Cat
        """
        cat = Cat('Whiskers', 'Grey')
        self.assertEqual(cat._color, 'Grey')
        self.assertEqual(cat.num_legs, 4)
        self.assertNotEqual(cat.make_sound(), 'Woof!')
        self.assertEqual(cat._name, 'Whiskers')
        self.assertIsInstance(cat, Mammal)

        self.assertRaises(TypeError, Animal.check_correct, 12)
        self.assertRaises(AssertionError, Cat.check_correct, "12")


    def test_FlyAnimal(self):
        """
        Testing FlyAnimal class
        """
        flying_animal = FlyingAnimal('generic')
        self.assertEqual(flying_animal._name, 'generic')
        self.assertRaises(TypeError, FlyingAnimal.check_correct, "12")

    def test_bird(self):
        """
        Testing class Bird
        """
        bird = Bird('generic')
        self.assertEqual(bird._name, 'generic')
        self.assertEqual(bird.make_sound(), 'Chirp!')
        self.assertEqual(bird.wingspan, 0)

    def test_Parrot(self):
        """
        Testing Parrot class
        """
        parrot = Parrot('Polly', 'English')
        self.assertEqual(parrot._name, 'Polly')
        self.assertEqual(parrot._language, 'English')
        self.assertEqual(parrot.wingspan, 20)
        self.assertEqual(parrot.make_sound(), 'Polly wants a cracker!')




if __name__ == "__main__":
    unittest.main()