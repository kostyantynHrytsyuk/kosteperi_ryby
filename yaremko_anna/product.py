class Product:
    def __init__(self, name, price):
        'initialization of variables'
        self._price = price
        self.name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        'checks price'
        if price < 0:
            raise ValueError("Price have to be >0")
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        'checks name of product'
        if not name.isalpha():
            raise ValueError("Name should contain only letters")
        self._name = name


class Clothing(Product):
    def __init__(self,name, price,  size, gender):
        'initialization of variables'
        super().__init__(name, price)
        self.size = size
        self.gender = gender
    
    def __str__(self):
        'info about clothes'
        return f'This {self.name} is for {self.gender} with size{self.size}'
    
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        example_size=['XS','S','M','L','XL']
        if size not in example_size:
            raise ValueError("Size can only be XS,S,M,L,XL ")
        self._size = size

class Nutrition(Product):
    type_of=None
    def __init__(self,name, price):
        'initialization of variables'
        super().__init__(name, price)


class Food(Nutrition):
    def __init__(self,name, price):
        'initialization of variables'
        super().__init__(name, price)
    type_of = "Food"
    
    def __str__(self):
        return f'This {self.name} is {self.type_of} and costs {self.price}'


class Drink(Nutrition):
    def __init__(self, name, price):
        'initialization of variables'
        super().__init__(name, price)
    type_of = "Drink"

    def __str__(self):
        return f'This {self.name} is {self.type_of} and costs {self.price}'

class Book(Product):
    def __init__(self, name, price, genre, page_count):
        'initialization of variables'
        super().__init__(name, price)
        self.genre = genre
        self.page_count = page_count

    def __str__(self):
        'info about book'
        return f"{self.name} ({self.genre}) - {self.page_count} pages"

class Basket:
    def __init__(self):
        'initialization of variables'
        self.products = {}

    def add_product(self, name, quantity=1):
        'adds products to a basket'
        if name in self.products:
            self.products[name] += quantity
        else:
            self.products[name] = quantity

    def remove_product(self, name, quantity=1):
        'removes product from a basket'
        if name in self.products:
            if self.products[name] <= quantity:
                del self.products[name]
            else:
                self.products[name] -= quantity
        else:
            return f'In basket there is no {name.lower()} '

    @staticmethod
    def get_total_price(products):
        'calculates price'
        suma = 0
        for name, quantity in products.items():
            suma += name.price * quantity
        return suma




