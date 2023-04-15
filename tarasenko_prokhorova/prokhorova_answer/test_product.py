"""Testing"""
import unittest
from product import Product, Clothing, Basket, Food, Drink, Book, Nutrition

class TestProduct(unittest.TestCase):
    """testing"""
    def test_product_creation(self):
        """testing"""
        p = Product('Dress', 25)
        self.assertEqual(p.name, 'Dress')
        self.assertEqual(p._price, 25)

    def test_negative_price(self):
        """testing"""
        with self.assertRaises(ValueError) as context:
            p = Product('Dress', -20)
        self.assertEqual(str(context.exception), 'Price have to be >0')

    def test_name_property(self):
        """testing"""
        p = Product('Dress', 25)
        p.name = 'Shirt'
        self.assertEqual(p.name, 'Shirt')

    def test_name_validation(self):
        """testing"""
        p = Product('Dress', 25)
        with self.assertRaises(ValueError) as context:
            p.name = 'Dres2s'
        self.assertEqual(str(context.exception), 'Name should contain only letters')

class TestClothing(unittest.TestCase):
    """testing"""
    def test_clothing_creation(self):
        """testing"""
        trousers = Clothing('Trousers', 22, 'L', 'Men')
        self.assertEqual(trousers.name, 'Trousers')
        self.assertEqual(trousers.price, 22)
        self.assertEqual(trousers.size, 'L')
        self.assertEqual(trousers.gender, 'Men')

    def test_invalid_size(self):
        """testing"""
        with self.assertRaises(ValueError) as context:
            a = Clothing('Shirt', 20, 'XXS', 'Men')
        self.assertEqual(str(context.exception), 'Size can only be XS,S,M,L,XL ')

class TestFoodDrinkBook(unittest.TestCase):
    """testing"""
    def test_food_drink_book_creation(self):
        """testing"""
        n = Nutrition("Nutrition", 10)
        f = Food("Food", 20)
        d = Drink("Drink", 30)
        self.assertIsInstance(n, Nutrition)
        self.assertIsInstance(f, Food)
        self.assertIsInstance(d, Drink)

        f = Food('Ice cream', 1.5)
        self.assertEqual(f.name, 'Ice cream')
        self.assertEqual(f.price, 1.5)
        self.assertEqual(f.type_of, 'Food')

        d = Drink('Juice', 3)
        self.assertEqual(d.name, 'Juice')
        self.assertEqual(d.price, 3)
        self.assertEqual(d.type_of, 'Drink')

        b = Book('Death on the Nile', 10, 'Detective', 123)
        self.assertEqual(b.name, 'Death on the Nile')
        self.assertEqual(b.price, 10)
        self.assertEqual(b.genre, 'Detective')
        self.assertEqual(b.page_count, 123)
        self.assertEqual(str(b), 'Death on the Nile (Detective) - 123 pages')

class TestBasket(unittest.TestCase):
    """testing"""
    def test_basket_operations(self):
        """testing"""
        basket = Basket()
        # adds product
        basket.add_product('Trousers', 2)
        self.assertEqual(basket.products, {'Trousers': 2})

        # adds same product
        basket.add_product('Trousers', 3)
        self.assertEqual(basket.products, {'Trousers': 5})

        # adds another type of product
        basket.add_product('Dress', 3)
        self.assertEqual(basket.products, {'Trousers': 5,'Dress': 3})

        # remove product
        basket.remove_product('Trousers', 2)
        self.assertEqual(basket.products, {'Trousers': 3,'Dress': 3})
        basket.remove_product('Trousers', 2)
        self.assertEqual(basket.products, {'Trousers': 1,'Dress': 3})
        basket.remove_product('Trousers', 1)
        basket.remove_product('Dress', 3)
        self.assertEqual(basket.products, {})
        self.assertEqual(basket.remove_product('Trousers', 1), 'In basket there is no trousers ')

        # calculates suma
        trousers = Product('Trousers', 20)
        lipton=Product('lipton', 3)
        basket.add_product(trousers, 2)
        basket.add_product(lipton, 4)
        self.assertEqual(basket.get_total_price(basket.products), 52)
if __name__ == '__main__':
    unittest.main()
