"""
classes for Anya Yaremko's asserts
"""
class Product:
    """A class representing a product.

    Attributes:
        name (str): The name of the product.
        _price (int): The price of the product.
    """

    def __init__(self, name: str, price: int) -> None:
        """Initializes an instance of the Product class with a name and a price."""
        if price < 0:
            raise ValueError('Price have to be >0')
        self.name = name
        self._price = price

    @property
    def price(self):
        """Returns the price of the product."""
        return self._price


class Clothing(Product):
    """A class representing a clothing product.

    Attributes:
        size (str): The size of the clothing.
        gender (str): The gender the clothing is intended for.
    """

    def __init__(self, name: str, price: int, size: str, gender: str) -> None:
        """Initializes an instance of the Clothing class with a name,
        a price, a size, and a gender."""
        super().__init__(name, price)
        if size not in ('XS','S','M','L','XL'):
            raise ValueError('Size can only be XS,S,M,L,XL ')
        self.size = size
        self.gender = gender


class Nutrition(Product):
    """A class representing a nutritional product."""

    type_of = None


class Basket:
    """A class representing a basket of products.

    Attributes:
        products (dict): A dictionary of the products in the basket and their amounts.
    """

    def __init__(self):
        'initialization of products'
        self.products = {}

    def add_product(self, prod: str, amount: int):
        """Adds a product and its amount to the basket."""
        if prod not in self.products:
            self.products[prod] = amount
        else:
            self.products[prod] += amount

    def remove_product(self, prod: str, amount: int):
        """Removes a product and its amount from the basket."""
        if prod not in self.products:
            return f'In basket there is no {prod.lower()} '
        self.products[prod] -= amount
        if self.products[prod] <= 0:
            del self.products[prod]

    def get_total_price(self, products: dict):
        """Returns the total price of the products in the basket."""
        return sum(i.price*products[i] for i in products)


class Food(Nutrition):
    """A class representing a food product."""

    type_of = 'Food'


class Drink(Nutrition):
    """A class representing a drink product."""

    type_of = 'Drink'


class Book(Product):
    """A class representing a book product.

    Attributes:
        genre (str): The genre of the book.
        page_count (int): The number of pages in the book.
    """

    def __init__(self, name: str, price: int, genre: str, pages: int) -> None:
        """Initializes an instance of the Book class with a name,
        a price, a genre, and a page count."""
        super().__init__(name, price)
        self.genre = genre
        self.page_count = pages

    def __str__(self) -> str:
        """Returns a string representation of a Book instance."""
        return f'{self.name} ({self.genre}) - {self.page_count} pages'
