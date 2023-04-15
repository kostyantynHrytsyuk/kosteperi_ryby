class Product:
    
    def __init__(self, name: str, price: int) -> None:
        """
        Initialize class Product
        """
        self._name = name
        self._price = self.check_price(price)

    @staticmethod
    def check_price(price: int):
        """
        Check price
        """
        if price > 0:
            return price
        else:
            raise ValueError('Price have to be >0')
    @property
    def price(self):
        return self._price
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name.isalpha():
            raise ValueError("Name should contain only letters")
        self._name = name

class Clothing(Product):
    
    def __init__(self, name: str, price: int, size:str, gender:str) -> None:
        super().__init__(name, price)
        self._size = size
        self.gender = gender

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size not in ['XS','S','M','L','XL']:
            raise ValueError("Size can only be XS,S,M,L,XL ")
        self._size = size

    @property
    def price(self):
        return self._price

class Nutrition(Product):

    def __init__(self, name: str, price: int) -> None:
        super().__init__(name, price)

class Food(Product):
    type_of = 'Food' 
    
    def __init__(self, name: str, price: int) -> None:
        super().__init__(name, price)

class Drink(Product):
    type_of = 'Drink'

    def __init__(self, name: str, price: int) -> None:
        super().__init__(name, price)


class Book(Product):
    
    def __init__(self, name: str, price: int, genre:str, page_count:str) -> None:
        super().__init__(name, price)
        self.genre = genre
        self.page_count = page_count

    def __str__(self) -> str:
        """
        Returns string
        """
        return f'{self.name} ({self.genre}) - {self.page_count} pages'

class Basket:
    
    def __init__(self) -> None:
        """
        Initialize class Basket
        """
        self.products = {}

    def add_product(self, name:str, number:int):
        if not name in self.products.keys():
            self.products[name] = number
        else:
            self.products[name] += number

    def remove_product(self, name:str, number:int):
        if name in self.products.keys():
            if self.products[name] <= number:
                self.products[name] -= number
                del self.products[name]
            else:
                self.products[name] -= number
        else:
            return 'In basket there is no trousers '

    @staticmethod
    def get_total_price(basket):
        return sum([product.price * basket[product] for product in basket])
