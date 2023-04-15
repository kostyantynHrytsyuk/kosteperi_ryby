import unittest
from product import Product, Clothing, Food, Drink, Book, Basket

class TestProduct(unittest.TestCase):
    def test_init(self):
        product = Product('Test Product', 10)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 10)
    
    def test_price_negative(self):
        with self.assertRaises(ValueError):
            product = Product('Negative Price', -10)

class TestClothing(unittest.TestCase):
    def test_init(self):
        clothing = Clothing('Test Clothing', 20, 'M', 'Male')
        self.assertEqual(clothing.name, 'Test Clothing')
        self.assertEqual(clothing.price, 20)
        self.assertEqual(clothing.size, 'M')
        self.assertEqual(clothing.gender, 'Male')
    
    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            clothing = Clothing('Invalid Size', 30, 'XXL', 'Female')

class TestFood(unittest.TestCase):
    def test_type(self):
        food = Food('Test Food', 5)
        self.assertEqual(food.type_of, 'Food')

class TestDrink(unittest.TestCase):
    def test_type(self):
        drink = Drink('Test Drink', 3)
        self.assertEqual(drink.type_of, 'Drink')

class TestBook(unittest.TestCase):
    def test_init(self):
        book = Book('Test Book', 15, 'Fiction', 200)
        self.assertEqual(book.name, 'Test Book')
        self.assertEqual(book.price, 15)
        self.assertEqual(book.genre, 'Fiction')
        self.assertEqual(book.page_count, 200)
    
    def test_str(self):
        book = Book('Test Book', 15, 'Fiction', 200)
        self.assertEqual(str(book), 'Test Book (Fiction) - 200 pages')

class TestBasket(unittest.TestCase):
    def setUp(self):
        self.basket = Basket()

    def test_add_product(self):
        self.basket.add_product('Test Product', 2)
        self.assertEqual(self.basket.products, {'Test Product': 2})

    def test_add_existing_product(self):
        self.basket.add_product('Test Product', 2)
        self.basket.add_product('Test Product', 3)
        self.assertEqual(self.basket.products, {'Test Product': 5})

    def test_remove_product(self):
        self.basket.add_product('Test Product', 2)
        self.basket.remove_product('Test Product', 1)
        self.assertEqual(self.basket.products, {'Test Product': 1})
        self.basket.remove_product('Test Product', 1)
        self.assertEqual(self.basket.products, {})

    def test_remove_nonexisting_product(self):
        self.assertEqual(self.basket.remove_product('Nonexisting Product', 1), 'In basket there is no nonexisting product ')

    def test_get_total_price(self):
        prod_1 = Product('Test Product 1', 5)
        self.basket.add_product(prod_1, 6)
        prod_2 = Product('Test Product 2', 3)
        self.basket.add_product(prod_2, 3)
        self.assertEqual(self.basket.get_total_price(self.basket.products), 39)

if __name__ == '__main__':
    unittest.main()
