class OrderProcessor():
    
    def __init__(self) -> None:
        # menginisiasi list kosong untuk menyimpan pesanan
        self.list_pesanan = []
        pass
    
    def add_order(self, order):
        # menambah pesanan kedalam list pesanan..
        self.list_pesanan.append(order)
        pass
    
    def calculate_total_revenue(self):
        # menghitung dan mengembalikan total pendapatan (jumlah total) untuk semua pesanan dalam list
        total = 0
        for x in self.list_pesanan:
            total += x.total_amount
        return total
    
    def calculate_total_tax(self,tax_rate):
        # menghitung dan mengembalikan total pendapatan (jumlah total) untuk semua pesanan dalam list
        total = 0
        for x in self.list_pesanan:
            total += x.calculate_tax(tax_rate)
        return total
    
    def display_order(self):
        # menampilkan rincian semua pesanan dalam list
        for x in self.list_pesanan:
            print(x.display_order())