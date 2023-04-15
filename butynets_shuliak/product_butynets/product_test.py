import unittest
from product import Product, Clothing, Basket, Food, Drink, Book, Nutrition


class TestProduct(unittest.TestCase):

    def test_product(self):

        product1 = Product('Dress', 25)
        self.assertRaises(ValueError, Product.check_price, -20)
        with self.assertRaises(ValueError):
            product1.name = 'Jeans123'
        self.assertEqual(Product.check_price(10), 10)

        name = 'Jeans'
        product1.name = name
        self.assertEqual(product1.name, name)

    def test_clothing(self):

        clothing = Clothing('Shirt', 50, 'M', 'Male')

        self.assertEqual(clothing.price, 50)
        with self.assertRaises(ValueError):
            clothing.size = 'Je'
        self.assertEqual(clothing.gender, 'Male')
        self.assertEqual(clothing.size, 'M')
        self.assertEqual(clothing._size, 'M')

    def test_basket(self):

        basket1 = Basket()
        basket1.add_product('Trousers', 3)
        basket1.add_product('Dress', 3)
        self.assertEqual(basket1.products, {'Trousers': 3,'Dress': 3})

        basket1.remove_product('Trousers', 2)
        basket1.remove_product('Dress', 3)
        self.assertEqual(basket1.products, {'Trousers': 1})
        basket1.remove_product('Trousers', 1)
        self.assertEqual(basket1.products, {})
        self.assertEqual(basket1.remove_product('Trousers', 1), 'In basket there is no trousers ')

        self.assertEqual(basket1.get_total_price(basket1.products), 0)

        basket2 = Basket()
        trousers = Product('Trousers', 20)
        lipton=Product('lipton', 3)
        basket2.add_product(trousers, 2)
        basket2.add_product(lipton, 4)
        self.assertEqual(basket2.get_total_price(basket2.products), 52)

    def test_book(self):

        book1 = Book('Death on the Nile', 10, 'Detective', 123)
        self.assertEqual(book1.name, 'Death on the Nile')
        self.assertEqual(book1.price, 10)
        self.assertEqual(book1.genre, 'Detective')
        self.assertEqual(str(book1), 'Death on the Nile (Detective) - 123 pages')

    def test_isisnstance(self):

        n = Nutrition("Nutrition", 10)
        self.assertIsInstance(n, Product)
        f = Food("Food", 20)
        self.assertIsInstance(f, Product)
        d = Drink("Drink", 30)
        self.assertIsInstance(d, Product)

if __name__ == "__main__":
    unittest.main()