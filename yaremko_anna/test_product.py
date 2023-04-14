from product import Product, Clothing, Basket, Food, Drink, Book, Nutrition
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
    assert trousers.price == 22
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
    assert f.price == 1.5
    assert f.type_of == 'Food'

def test_drink_class():
    # Creates Drink
    d = Drink('Juice', 3)
    assert d.name == 'Juice'
    assert d.price == 3
    assert d.type_of == 'Drink'

def test_book_class():
    # create Book
    b = Book('Death on the Nile', 10, 'Detective', 123)
    assert b.name == 'Death on the Nile'
    assert b.price == 10
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




