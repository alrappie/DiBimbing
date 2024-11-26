class Order():
    
    def __init__(self, order_id:str, customer_name:str, order_date:str, total_amount:float):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount
    
    def calculate_tax(self,tax_rate):
        return self.total_amount * tax_rate / 100
    
    def display_order(self):
        # mencetak detail pesanan 
        return f"""
        ----------------------------------------
        Detail Pesanan
        ----------------------------------------
        Order ID      : {self.order_id}
        Customer Name : {self.customer_name}
        Order Date    : {self.order_date}
        Total Amount  : {self.total_amount}
        ----------------------------------------
        """