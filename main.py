class Product:
    def __init__(self, id, name, description, cost, quantity, sales_margin):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.quantity = quantity
        self.sales_margin = sales_margin
        self.sales_price = self.calculate_sales_price()

    def calculate_sales_price(self):
        return self.cost / (1 - self.sales_margin)

class ProductRegistry:
    def __init__(self):
        self.products = {}

    def register_product(self, product):
        self.products[product.id] = product

    def print_products(self):
        for product_id, product in self.products.items():
            print(f"Product ID: {product_id}")
            print(f"Name: {product.name}")
            print(f"Description: {product.description}")
            print(f"Cost: ${product.cost}")
            print(f"Quantity: {product.quantity}")
            print(f"Sales Price: ${product.sales_price}")
            print("--------------------------")

# Example usage:
registry = ProductRegistry()
product1 = Product(1, "Product1", "Description1", 10.0, 100, 0.2)
product2 = Product(2, "Product2", "Description2", 15.0, 50, 0.3)

registry.register_product(product1)
registry.register_product(product2)

registry.print_products()

