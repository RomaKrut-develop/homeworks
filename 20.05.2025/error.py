import logging
from dataclasses import dataclass
from abc import ABC, abstractmethod
from decorator import decorator

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", encoding="UTF-8")

@dataclass 
class Product:
    id: int
    name: str
    price: float
    quantity: int

    def __post_init__(self):
        logging.info("Product: {self.name} (ID: {self.id})")

class ProdcutOperation(ABC):
    @abstractmethod
    def update_price(self, new_price: float) -> None:
        pass

    @abstractmethod
    def apply_discount(self, discount: float) -> None:
        pass

class ProductWithDiscount(Product, ProdcutOperation):
    def update_price(self, new_price: float) -> None:
        logging.info(f"Price {self.price} has been changed for product {self.name} on {new_price}")
        self.price = new_price

    def apply_discount(self, discount: float) -> None:
        discount_price = self.price * (discount / 100)
        logging.info(f"{self.name} has now {discount} discount, it's costs {discount_price}")

@decorator
def log_function(func, *args, **kwargs):
    logging.info(f"Function {func.__name__} with args: {args} and {kwargs}")
    result = func(*args, **kwargs)
    logging.info(f"Function {func.__name__} return result: {result}")
    return result

@log_function
def create_product(id: int, name: str, price: float, quantity: int) ->  ProductWithDiscount:
    return ProductWithDiscount(id, name, price, quantity)

@log_function
def update_product_price(product: ProductWithDiscount, new__price: float):
    product.update_price(new__price)   

product = create_product(1, input(), 20000, 500)
update_product_price(product, 19990)
product.apply_discount(10)