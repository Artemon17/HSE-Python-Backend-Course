from models.product import Product


def comp(prod):
    return prod.price

def get_ordered_products_by_price(products: list[Product]) -> list[Product]:
    return sorted(products, key=comp, reverse=True)