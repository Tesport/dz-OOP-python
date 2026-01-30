class Basket:
    def __init__(self):
        self._inner = []

    def add_to_cart(self, product):
        self._inner.append(product)

    @ property
    def inner(self):
        return self._inner


class User:
    def __init__(self, login, password):
        self._login = login
        self.__password = password
        self._basket = Basket()

    @property
    def basket(self):
        return self._basket


class Category:
    def __init__(self, catname):
        self._cat_name = catname
        self._products = []

    def add_to_cat(self, product):
        self._products.append(product)

    @property
    def prods(self):
        return self._products


class Product:
    def __init__(self, name, price, rating, category):
        self._name = name
        self._price = price
        self._rating = rating
        self._category = category
        category.add_to_cat(self)


def show_prods(container):
    n = len(container)
    for i in range(n):
        print(f"Товар: {container[i]._name} - {container[i]._price}руб. ({container[i]._rating}/10*)")


print("\nProducts list: ")
computer_devices = Category("Computer_Devices")
mouse_blyadi = Product("Компьютерная игровая мышь Blyadi", 1200, 10, computer_devices)
keyboard_deblender = Product("Клавиатура Defraktor", 2200, 8, computer_devices)
headphones_imbapushka = Product("Наушники Chepuha", 700, 5, computer_devices)
show_prods(computer_devices.prods)

print("\nUser n1 basket:")
user1 = User("AbobusGlobus", "NeSkazhu2281488")
user1.basket.add_to_cart(mouse_blyadi)
show_prods(user1.basket.inner)

print("\nUser n2 basket:")
user2 = User("Abobus2", "NeSkazhu2281337")
user2.basket.add_to_cart(keyboard_deblender)
user2.basket.add_to_cart(headphones_imbapushka)
show_prods(user2.basket.inner)
