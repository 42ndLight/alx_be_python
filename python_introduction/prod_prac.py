class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def value_inv(self):
        return self.price * self.quantity
    
def total_stock_value(products):
    total =  sum(product.value_inv() for product in products)
    return total

product1 = Product("Phone", 340, 10) 
product2 = Product("Laptop", 1420, 3)
product3 = Product("Tablet", 450, 5)

products = [product1, product2, product3]

print(total_stock_value(products))
print(product1.value_inv())