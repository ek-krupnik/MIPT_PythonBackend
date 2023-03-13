class Product:
    def __init__(self, name: str, category: str, price: int) -> None:
        self.name = name
        self.category = category
        self.price = price
        self.sale = 0

    def edit_category(self, new_category: str) -> None:
        self.category = new_category

    def edit_price(self, new_price: int) -> None:
        self.price = new_price

    def set_sale(self, sale: int) -> None:
        self.sale = sale

    def cancel_sale(self) -> None:
        self.sale = 0

    def get_price(self) -> int:
        return self.price - self.price * self.sale / 100

    def __repr__(self) -> str:
        rep = f'Product {self.name} in category {self.category}. Price {self.price} and discount {self.sale}%'
        return rep
