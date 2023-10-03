from models.customer import Customer
from models.inventory import Inventory
from models.payment import Payment
from models.product import Product
from models.shopping_cart import ShoppingCart


p1 = Product("iPhone", "New iPhone", 999.99, 10)
inventory = Inventory()
inventory.add_product(p1, 10)
c1 = Customer("John Smith", "123 Main St", "johnsmith@email.com")
cart = ShoppingCart()
cart.add_product(p1)

if inventory.is_in_stock(p1):
    print("Product is in stock")
else:
    print("Product is out of stock")

print("Total cost: Rs", cart.total_cost())

payment = Payment(cart.total_cost(), "Credit Card")
print("Payment amount: Rs", payment.amount)
print("Payment method: ", payment.payment_method)