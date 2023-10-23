from client import Client

class Order:
    def __init__(self,total_price,status,client) -> None:
        self.total_price = total_price
        self.status = status
        self.Client = client