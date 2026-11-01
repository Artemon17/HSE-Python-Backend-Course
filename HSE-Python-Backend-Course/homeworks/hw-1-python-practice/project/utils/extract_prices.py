from models.product import Product


def extract_prices(products: list[Product]) -> list[float]:
    return [prod.price for prod in products]
