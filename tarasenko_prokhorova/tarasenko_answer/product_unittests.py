import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.basket = Basket()
        self.p1 = Product('apple', 5)
        self.p2 = Product('banana', 2)

    def test_product_init(self):
        self.assertRaises(ValueError, lambda: Product('apple', 0))
        self.assertRaises(ValueError, lambda: Product(123, 10))
        self.assertRaises(ValueError, lambda: Product('coke1', 5))
    
    def test_clothing_init(self):
        self.assertRaises(ValueError, lambda:Clothing('tshirt', 20, 'MN', 'F'))
        self.assertRaises(ValueError, lambda:Clothing('tshirt', 20, 'm', 'F'))
    
    def test_add_product(self):
        self.basket.add_product(self.p1, 2)
        self.assertEqual(self.basket.products, {self.p1: 2})
        self.basket.add_product(self.p2, 3)
        self.assertEqual(self.basket.products, {self.p1: 2, self.p2: 3})
        self.basket.add_product(self.p1, 4)
        self.assertEqual(self.basket.products, {self.p1: 6, self.p2: 3})
    
    def test_remove_product(self):
        self.basket.add_product(self.p1, 2)
        self.basket.add_product(self.p2, 3)
        self.basket.remove_product(self.p1, 1)
        self.assertEqual(self.basket.products, {self.p1: 1, self.p2: 3})
        self.basket.remove_product(self.p1, 2)
        self.assertEqual(self.basket.products, {self.p2: 3})
    
    def test_get_total_price(self):
        self.basket.add_product(self.p1, 2)
        self.basket.add_product(self.p2, 3)
        self.assertEqual(self.basket.get_total_price(self.basket.products), 16)
        self.basket.remove_product(self.p1, 1)
        self.assertEqual(self.basket.get_total_price(self.basket.products), 11)

if __name__ == '__main__':
    unittest.main()
