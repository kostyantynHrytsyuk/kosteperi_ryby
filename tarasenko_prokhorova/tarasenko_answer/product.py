"""product module"""
class Product:
    """product class"""
    def __init__(self, name, price):
        self.name = name
        self._price = price
        if not(self._price > 0 and isinstance(self.name, str)):
            raise ValueError('Price have to be >0')
        for char in self.name:
            if char.isdigit() is True:
                raise ValueError('Name should contain only letters')

class Clothing(Product):
    """clothing class"""
    def __init__(self, name, price, size, gender):
        self.name = name
        self.price = price
        self.size = size
        self.gender = gender
        if size not in ['XS', 'S', 'M', 'L', 'XL']:
            raise ValueError('Size can only be XS,S,M,L,XL ')

class Food:
    """food class"""
    type_of = 'Food'
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Nutrition(Food):
    """nutrition class"""
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Drink(Food):
    """drink class"""
    type_of = 'Drink'
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Book:
    """book class"""
    def __init__(self, name, price, genre, page_count):
        self.name = name
        self.price = price
        self.genre = genre
        self.page_count = page_count
    def __str__(self):
        return f'{self.name} ({self.genre}) - {self.page_count} pages'

class Basket:
    """basket class"""
    def __init__(self):
        self.products = {}
    def add_product(self, product, quantity):
        """add product to basket"""
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products.update({product: quantity})
    def remove_product(self, product, quantity):
        """remove product from basket"""
        if product in self.products:
            self.products[product] -= quantity
            if self.products[product] <= 0:
                del self.products[product]
        else:
            return (f'In basket there is no {product.lower()} ')
    def get_total_price(self, basket):
        """get total price of basket"""
        total_price = 0
        for product in basket:
            total_price += self.products[product] * product._price
        return total_price
