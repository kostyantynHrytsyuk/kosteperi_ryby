"""Product"""
class Product:
    """Product"""
    def __init__(self, name, price):
        self._name = name
        self._price = price
        if price <= 0:
            raise ValueError('Price have to be >0')
    @property
    def name(self):
        """Name"""
        return self._name
    @name.setter
    def name(self, name):
        if not name.isalpha():
            raise ValueError('Name should contain only letters')
        self._name = name
    @property
    def price(self):
        """Price"""
        return self._price
    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError('Price have to be >0')
        self._price = price

class Clothing(Product):
    """Clothing"""
    def __init__(self, name, price, size, gender):
        super().__init__(name, price)
        self._size = size
        self._gender = gender
        sizes = ['XS', 'S', 'M', 'L', 'XL']
        if size not in sizes:
            raise ValueError('Size can only be XS,S,M,L,XL ')
    @property
    def size(self):
        """size"""
        return self._size
    @size.setter
    def size(self, size):
        sizes = ['XS', 'S', 'M', 'L', 'XL']
        if size not in sizes:
            raise ValueError('Size can only be XS,S,M,L,XL ')
        self._size = size     
    @property
    def gender(self):
        """gender"""
        return self._gender

class Food(Product):
    """food"""
    def __init__(self, name, price):
        super().__init__(name, price)
        self._type_of = 'Food'
    @property
    def type_of(self):
        """type"""
        return self._type_of

class Drink(Product):
    """drink"""
    def __init__(self, name, price):
        super().__init__(name, price)
        self._type_of = 'Drink'
    @property
    def type_of(self):
        """type"""
        return self._type_of

class Book(Product):
    """book"""
    def __init__(self, name, price, genre, page_count):
        super().__init__(name, price)
        self._genre = genre
        self._page_count = page_count
    @property
    def genre(self):
        """genre"""
        return self._genre
    @property
    def page_count(self):
        """page_count"""
        return self._page_count
    def __str__(self):
        return f"{self._name} ({self._genre}) - {self._page_count} pages"

class Nutrition(Product):
    """nutrition"""
    def __init__(self, name, price):
        super().__init__(name, price)

class Basket:
    """basket"""
    def __init__(self):
        self.products = {}
        self.price=0
    def add_product(self, product, quantity=1):
        """add product"""
        if isinstance(product, str):
            if product in self.products:
                self.products[product] += quantity
            else:
                self.products[product] = quantity
        else:
            if product.name in self.products:
                self.products[product.name] += quantity
            else:
                self.products[product.name] = quantity
            self.price+=product.price*quantity
    def remove_product(self, product, quantity=1):
        """remove product"""
        if isinstance(product, str):
            if product in self.products:
                if self.products[product] > quantity:
                    self.products[product] -= quantity
                elif self.products[product] == quantity:
                    self.products.pop(product)
                else:
                    return f'Invalid quantity. There are only {self.products[product]} {product}\
                         in the basket'
                if isinstance(product, Product):
                    self.price-=product.price*quantity
            else:
                return f'In basket there is no {product.lower()} '
    def get_total_price(self, products):
        """get total price"""
        if products==self.products:
            return self.price
