import unittest

from  product import Product, Clothing, Nutrition , Food,  Drink, Book, Basket


import unittest

class TestProduct(unittest.TestCase):
    def test_name_check(self):
        p = Product('shirt', 10.99)
        self.assertEqual(p.name_check('shirt'), 'shirt')
        with self.assertRaises(ValueError):
            prod  = Product('Dr33ess', 25)

    def test_price_check(self):
        p = Product('shirt', 10.99)
        self.assertEqual(p.price_check(10.99), 10.99)
        with self.assertRaises(ValueError):
            p.price_check(-5)

class TestClothing(unittest.TestCase):
    def test_size_check(self):
        c = Clothing('shirt', 10.99, 'S', 'M')
        self.assertEqual(c.size_check('S'), 'S')
        with self.assertRaises(ValueError):
            c.size_check('XXL')

    def test_gender_check(self):
        c = Clothing('shirt', 10.99, 'S', 'M')
        self.assertEqual(c.gender_check('M'), 'M')
        with self.assertRaises(ValueError):
            c.gender_check(65)

class TestBook(unittest.TestCase):
    def test_genre_check(self):
        b = Book('The Great Gatsby', 12.99, 'Fiction', 180)
        self.assertEqual(b.genre_check('Fiction'), 'Fiction')
        with self.assertRaises(ValueError):
            b.genre_check('Science123')

    def test_count_check(self):
        b = Book('The Great Gatsby', 12.99, 'Fiction', 180)
        self.assertEqual(b.count_check(180), 180)
        with self.assertRaises(ValueError):
            b.count_check(-5)

class TestBasket(unittest.TestCase):
    def test_add_product(self):
        basket = Basket()
        basket.add_product('Shirt', 2)
        basket.add_product('Shirt', 6)
        self.assertEqual(basket.products, {'Shirt': 8})
        basket.add_product('Dress', 3)

    def test_remove_product(self):
        basket = Basket()
        basket.add_product('skirt', 3)
        basket.remove_product('skirt', 2)
        self.assertEqual(basket.products, {'skirt': 1})
        self.assertEqual(basket.remove_product('Trousers', 1), 'In basket there is no trousers ')
    
    def test_get_total_price(self):
        basket = Basket()
        book2 = Product('Harry Potter', 25)
        blouse = Product('Blouse', 50)
        basket.add_product(book2, 2)
        basket.add_product(blouse, 1)
        self.assertEqual(basket.get_total_price(basket.products), 100)

