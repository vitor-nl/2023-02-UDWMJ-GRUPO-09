from client import Client
from order import Order
from order_item import OrderItem

client = Client("Eduarda","Ilha","ldr45","44","Eduarda@gmail.com","F")
#print(client.firt_name)
order = Order(50,"status",client)
print(order.Client.firt_name)
orderi= OrderItem(1,50,order)
print(orderi.Order.Client.firt_name)