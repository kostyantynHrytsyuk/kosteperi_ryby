"""Implementation by Sofia Shuliak"""

class Product:
    def __init__(self, name, price) -> None:
        self.name = self.name_check(name)
        self._price = self.price_check(price)

    def name_check(self, name):
        """Checks name"""
        if not name.isdigit():
            return name
        else:
            raise ValueError('Name should contain only letters')

    def price_check(self, price):
        """Checks price"""
        if isinstance(price, (int, float)) and price > 0:
            return price
        else:
            raise ValueError('Price have to be >0')
        
    @property
    def get_price(self):
        return self._price

class Clothing(Product):
    def __init__(self, name, price, size, gender) -> None:
        super().__init__(name, price)
        self.size = self.size_check(size)
        self.gender = self.gender_check(gender)

    def size_check(self, size):
        """Checks size"""
        size_var = ['XS', 'S', 'M', 'L', 'XL']
        if isinstance(size, str) and size in size_var:
            return size
        else:
            raise ValueError('Size can only be XS,S,M,L,XL ')

    def gender_check(self, gender):
        """Checks gender input"""
        if isinstance(gender, str) and gender.isalpha():
            return gender
        else:
            raise ValueError('Enter gender correctly')


class Nutrition(Product):
    """Nutrition class"""
    def __init__(self, name, price) -> None:
        super().__init__(name, price)


class Food(Nutrition):
    def __init__(self, name, price) -> None:
        super().__init__(name, price)
        self.type_of = 'Food'

class Drink(Nutrition):
    def __init__(self, name, price) -> None:
        super().__init__(name, price)
        self.type_of = 'Drink'

class Book(Product):
    def __init__(self, name, price, genre, page_count:int) -> None:
        super().__init__(name, price)
        self.genre = self.genre_check(genre)
        self.page_count = self.count_check(page_count)

    def genre_check(self, genre):
        """Checks genre"""
        if isinstance(genre, str) and not genre.isdigit():
            return genre
        else:
            raise ValueError('Enter genre correctly')

    def count_check(self, page_count):
        """Checks page count"""
        if isinstance(page_count, int) and page_count > 0:
            return page_count
        else:
            raise ValueError('Page count has to be positive integer')

    def __str__(self) -> str:
        return f"{self.name} ({self.genre}) - {self.page_count} page{'s' if self.page_count > 1 else ''}"



class Basket:
    def __init__(self) -> None:
        self.products = {}
    
    def add_product(self, name, amount=1):
        """Adds products to basket"""
        if name in self.products:
            self.products[name] += amount
        else: self.products[name] = amount

    def remove_product(self, name, amount=1):
        """Removes products from basket"""
        if name not in self.products:
            return f'In basket there is no {name.lower()} '
        if name in self.products and self.products[name] <= amount:
            del self.products[name]
        else:
            self.products[name] -= amount

    @staticmethod
    def get_total_price(products):
        """Returns total price"""
        total = 0
        for name, amount in products.items():
            total += name._price * amount
        return total











def test_product_class():
    # create Product
    p = Product('Dress', 25)
    assert p.name == 'Dress'
    assert p._price == 25

    # checks price
    try:
        p = Product('Dress', -20)
    except ValueError as e:
        assert str(e) == 'Price have to be >0'

    # check name property
    p.name = 'Shirt'
    assert p.name == 'Shirt'

    # checks anme
    try:
        p.name = 'Dres2s'
    except ValueError as e:
        assert str(e) == 'Name should contain only letters'

def test_clothing_class():
    trousers = Clothing('Trousers', 22, 'L', 'Men')
    assert trousers.name == 'Trousers'
    assert trousers._price == 22
    assert trousers.size == 'L'
    assert trousers.gender == 'Men'

    try:
        a = Clothing('Shirt', 20, 'XXS', 'Men')
    except ValueError as e:
        assert str(e) == 'Size can only be XS,S,M,L,XL '

def test_nutrition_class():
    n = Nutrition("Nutrition", 10)
    f = Food("Food", 20)
    d = Drink("Drink", 30)

    assert isinstance(n, Nutrition)
    assert isinstance(f, Food)
    assert isinstance(d, Drink)

def test_food_class():
    # creates Food
    f = Food('Ice cream', 1.5)
    assert f.name == 'Ice cream'
    assert f._price == 1.5
    assert f.type_of == 'Food'

def test_drink_class():
    # Creates Drink
    d = Drink('Juice', 3)
    assert d.name == 'Juice'
    assert d._price == 3
    assert d.type_of == 'Drink'

def test_book_class():
    # create Book
    b = Book('Death on the Nile', 10, 'Detective', 123)
    assert b.name == 'Death on the Nile'
    assert b._price == 10
    assert b.genre == 'Detective'
    assert b.page_count == 123

    assert str(b) == 'Death on the Nile (Detective) - 123 pages'

def test_basket_class():
    # create Basket
    basket = Basket()

    # adds product
    basket.add_product('Trousers', 2)
    assert basket.products == {'Trousers': 2}

    # adds same product
    basket.add_product('Trousers', 3)
    assert basket.products == {'Trousers': 5}

    # adds another type of product
    basket.add_product('Dress', 3)
    assert basket.products == {'Trousers': 5,'Dress': 3}

    # remove product
    basket.remove_product('Trousers', 2)
    assert basket.products == {'Trousers': 3,'Dress': 3}
    basket.remove_product('Trousers', 2)
    assert basket.products == {'Trousers': 1,'Dress': 3}
    basket.remove_product('Trousers', 1)
    basket.remove_product('Dress', 3)
    assert basket.products == {}
    assert basket.remove_product('Trousers', 1) == 'In basket there is no trousers '

    # calculates suma
    trousers = Product('Trousers', 20)
    lipton=Product('lipton', 3)
    basket.add_product(trousers, 2)
    basket.add_product(lipton, 4)
    assert basket.get_total_price(basket.products) == 52



if __name__ == '__main__':
    test_product_class()
    test_clothing_class()
    test_nutrition_class()
    test_food_class()
    test_drink_class()
    test_book_class()
    test_basket_class()
