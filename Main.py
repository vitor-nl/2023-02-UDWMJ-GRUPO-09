from Cliente import Cliente
from Order import Order
from OrderItem import OrderItem

client = Cliente("Eduarda","Ilha","ldr45","44","Eduarda@gmail.com","F")
#print(client.firt_name)
order = Order(50,"status",client)
print(order.Cliente.firt_name)
orderi= OrderItem(1,50,order)
print(orderi.Order.Cliente.firt_name)