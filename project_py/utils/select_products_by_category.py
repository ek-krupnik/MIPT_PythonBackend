def select_products_by_category(products: list, category: str) -> list:
    return [product for product in products if product.category == category]
