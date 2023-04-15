import unittest

from animals import Animal, Mammal, Dog, Cat, FlyingAnimal, Bird, Parrot


class AnimalTests(unittest.TestCase):
    def test_animal_has_name(self):
        animal = Animal('Bob')
        self.assertEqual(animal._name, 'Bob')


class MammalTests(unittest.TestCase):
    def test_mammal_num_legs_is_none(self):
        mammal = Mammal('Bob')
        self.assertIsNone(mammal.num_legs)


class DogTests(unittest.TestCase):
    def test_dog_species_is_canis_lupus_familiaris(self):
        dog = Dog('Fido', 'Golden Retriever')
        self.assertEqual(dog.species, 'Canis lupus familiaris')

    def test_dog_num_legs_is_4(self):
        dog = Dog('Fido', 'Golden Retriever')
        self.assertEqual(dog.num_legs, 4)

    def test_dog_breed_property(self):
        dog = Dog('Fido', 'Golden Retriever')
        self.assertEqual(dog.breed, 'Golden Retriever')

    def test_dog_make_sound(self):
        dog = Dog('Fido', 'Golden Retriever')
        self.assertEqual(dog.make_sound(), 'Woof!')


class CatTests(unittest.TestCase):
    def test_cat_species_is_felis_catus(self):
        cat = Cat('Whiskers', 'Orange')
        self.assertEqual(cat.species, 'Felis catus')

    def test_cat_num_legs_is_4(self):
        cat = Cat('Whiskers', 'Orange')
        self.assertEqual(cat.num_legs, 4)

    def test_cat_color_property(self):
        cat = Cat('Whiskers', 'Orange')
        self.assertEqual(cat._color, 'Orange')

    def test_cat_make_sound(self):
        cat = Cat('Whiskers', 'Orange')
        self.assertEqual(cat.make_sound(), 'Meow!')


class FlyingAnimalTests(unittest.TestCase):
    def test_flying_animal_wingspan_property(self):
        flying_animal = FlyingAnimal('Bob')
        self.assertEqual(flying_animal.wingspan, 0)


class BirdTests(unittest.TestCase):
    def test_bird_make_sound(self):
        bird = Bird('Bob')
        self.assertEqual(bird.make_sound(), 'Chirp!')


class ParrotTests(unittest.TestCase):
    def test_parrot_species_is_psittaciformes(self):
        parrot = Parrot('Polly', 'English')
        self.assertEqual(parrot.species, 'Psittaciformes')

    def test_parrot_wingspan_property(self):
        parrot = Parrot('Polly', 'English')
        self.assertEqual(parrot.wingspan, 20)

    def test_parrot_language_property(self):
        parrot = Parrot('Polly', 'English')
        self.assertEqual(parrot._language, 'English')

    def test_parrot_make_sound(self):
        parrot = Parrot('Polly', 'English')
        self.assertEqual(parrot.make_sound(), 'Polly wants a cracker!')

if __name__ == '__main__':
    unittest.main()