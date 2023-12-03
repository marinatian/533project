# sales.py

class SalesManager:
    def __init__(self):
        self.sales_records = []

    def record_sale(self, product_id, quantity, price):
        self.sales_records.append({"product_id": product_id, "quantity": quantity, "price": price})

    def total_sales(self):
        return sum(record['price'] * record['quantity'] for record in self.sales_records)
