"""Testing"""
import unittest
from animals import Dog, Cat, Parrot, Bird
class TestAnimalClasses(unittest.TestCase):
    """Test animal"""
    def test_dog_breed(self):
        """test dog"""
        d = Dog('Rufus', 'Labrador Retriever')
        self.assertEqual(d.breed, 'Labrador Retriever')
        d.breed = 'German Shepherd'
        self.assertEqual(d.breed, 'German Shepherd')
        with self.assertRaises(TypeError):
            d.breed = 123

    def test_cat_color(self):
        """test cat"""
        c = Cat('Fluffy', 'gray')
        self.assertEqual(c.color, 'gray')
        c.color = 'black'
        self.assertEqual(c.color, 'black')
        with self.assertRaises(TypeError):
            c.color = 123

    def test_parrot_wingspan(self):
        """test parrot"""
        p = Parrot('Polly', 'English')
        self.assertEqual(p.wingspan, 20)
        p.wingspan = 25
        self.assertEqual(p.wingspan, 25)
        with self.assertRaises(TypeError):
            p.wingspan = 'twenty-five'

    def test_make_sound(self):
        """test make sound"""
        d = Dog('Rufus', 'Labrador Retriever')
        c = Cat('Fluffy', 'gray')
        b = Bird('Tweety')
        p = Parrot('Polly', 'English')
        self.assertEqual(d.make_sound(), 'Woof!')
        self.assertEqual(c.make_sound(), 'Meow!')
        self.assertEqual(b.make_sound(), 'Chirp!')
        self.assertEqual(p.make_sound(), 'Polly wants a cracker!')

if __name__ == '__main__':
    unittest.main()
