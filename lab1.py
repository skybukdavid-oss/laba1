class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.price:.2f} грн (залишок: {self.quantity})"


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if product.quantity <= 0:
            print("Товару немає в наявності.")
            return

        self.items.append(product)
        product.quantity -= 1
        print(f"Товар '{product.name}' додано до кошика.")

    def remove_product(self, name):
        for product in self.items:
            if product.name.lower() == name.lower():
                product.quantity += 1
                self.items.remove(product)
                print(f"Товар '{product.name}' видалено з кошика.")
                return

        print("Такого товару немає в кошику.")

    def show_cart(self):
        if not self.items:
            print("\nКошик порожній.")
            return

        print("\n--- КОШИК ---")

        # lambda використовується для сортування товарів
        sorted_items = sorted(self.items, key=lambda product: product.name)

        total = 0

        for product in sorted_items:
            print(f"{product.name} - {product.price:.2f} грн")
            total += product.price

        print(f"Загальна сума: {total:.2f} грн")

    def buy(self):
        if not self.items:
            print("Кошик порожній.")
            return

        total = sum(map(lambda product: product.price, self.items))

        print("\n--- ПОКУПКА ---")
        print(f"До сплати: {total:.2f} грн")

        self.items.clear()

        print("Дякуємо за покупку!")


class Store:
    ADMIN_LOGIN = "admin"
    ADMIN_PASSWORD = "1234"

    def __init__(self):
        self.products = [
            Product("Ноутбук", 25000.00, 5),
            Product("Мишка", 650.50, 10),
            Product("Клавіатура", 1200.99, 7),
            Product("Навушники", 1800.00, 6),
            Product("Монітор", 7500.75, 4)
        ]

        self.cart = Cart()

    def show_catalog(self):
        print("\n--- КАТАЛОГ ТОВАРІВ ---")

        # lambda для сортування каталогу за ціною
        sorted_products = sorted(
            self.products,
            key=lambda product: product.price
        )

        for index, product in enumerate(sorted_products, start=1):
            print(
                f"{index}. {product.name} - "
                f"{product.price:.2f} грн - "
                f"залишок: {product.quantity}"
            )

    def add_to_cart(self):
        self.show_catalog()

        name = input("\nВведіть назву товару: ")

        for product in self.products:
            if product.name.lower() == name.lower():
                self.cart.add_product(product)
                return

        print("Товар не знайдено.")

    def remove_from_cart(self):
        self.cart.show_cart()

        if self.cart.items:
            name = input("\nВведіть назву товару для видалення: ")
            self.cart.remove_product(name)

    def admin_login(self):
        print("\n--- ВХІД АДМІНІСТРАТОРА ---")

        login = input("Логін: ")
        password = input("Пароль: ")

        if login == self.ADMIN_LOGIN and password == self.ADMIN_PASSWORD:
            print("Вхід успішний!")
            self.show_stock()
        else:
            print("Неправильний логін або пароль.")

    def show_stock(self):
        print("\n--- ЗАЛИШКИ ТОВАРІВ ---")

        # lambda для сортування за кількістю
        sorted_products = sorted(
            self.products,
            key=lambda product: product.quantity,
            reverse=True
        )

        for product in sorted_products:
            print(
                f"{product.name}: "
                f"{product.quantity} шт. "
                f"({product.price:.2f} грн)"
            )

    def run(self):
        while True:
            print("\n========== МІНІ МАГАЗИН ==========")
            print("1. Переглянути каталог")
            print("2. Додати товар у кошик")
            print("3. Видалити товар з кошика")
            print("4. Переглянути кошик")
            print("5. Купити товари")
            print("6. Увійти як адміністратор")
            print("0. Вийти")

            choice = input("\nОберіть дію: ")

            if choice == "1":
                self.show_catalog()

            elif choice == "2":
                self.add_to_cart()

            elif choice == "3":
                self.remove_from_cart()

            elif choice == "4":
                self.cart.show_cart()

            elif choice == "5":
                self.cart.buy()

            elif choice == "6":
                self.admin_login()

            elif choice == "0":
                print("До побачення!")
                break

            else:
                print("Невірний вибір. Спробуйте ще раз.")


# Точка входу в програму
if __name__ == "__main__":
    store = Store()
    store.run()
