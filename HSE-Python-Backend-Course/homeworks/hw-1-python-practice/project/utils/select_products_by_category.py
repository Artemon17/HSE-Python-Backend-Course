from models.product import Product



def select_products_by_category(products: list[Product], category: str) -> list[Product]:
    return [prod for prod in products if prod.category == category]
