from Order import Order

class OrderItem:
    def __init__(self,quantity,unitary_price,order) -> None:
        self.quantity = quantity
        self.unitary_price = unitary_price
        self.Order = order
      #  self.product =product