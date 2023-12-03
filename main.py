# main.py
import sys
sys.path.append('/Users/chenshiyi/Desktop/Data533/SupermarketManagementSystem')

from inventory_management.products import ProductManager
from inventory_management.stock import StockManager, PerishableStockManager
from sales_management.sales import SalesManager
from sales_management.discounts import DiscountManager
# Initialize managers
product_manager = ProductManager()
stock_manager = StockManager()
perishable_stock_manager = PerishableStockManager()
sales_manager = SalesManager()
discount_manager = DiscountManager()
# Pre-load some data
initial_products = {
    "P001": {"name": "Milk", "price": 2.99},
    "P002": {"name": "Bread", "price": 1.99},
    "P003": {"name": "Eggs", "price": 3.50},
    "P004": {"name": "Apples", "price": 0.99},
    "P005": {"name": "Chicken", "price": 5.99},
    "P006": {"name": "Orange Juice", "price": 3.99},
    "P007": {"name": "Chocolate Bar", "price": 1.50},
    "P008": {"name": "Pasta", "price": 1.20},
    "P009": {"name": "Tomato Sauce", "price": 2.50},
    "P010": {"name": "Cheese", "price": 4.50},
    "P011": {"name": "Cereal", "price": 3.40},
    "P012": {"name": "Yogurt", "price": 0.80},
    "P013": {"name": "Butter", "price": 2.50},
    "P014": {"name": "Bananas", "price": 0.60},
    "P015": {"name": "Spinach", "price": 2.00}
}
initial_stock = {
    "P001": 100,  # 100 units of Milk
    "P002": 50,   # 50 units of Bread
    "P003": 200,  # 200 units of Eggs
    "P004": 75,   # 75 units of Apples
    "P005": 40,   # 40 units of Chicken
    "P006": 80,   # 80 units of Orange Juice
    "P007": 150,  # 150 units of Chocolate Bar
    "P008": 100,  # 100 units of Pasta
    "P009": 60,   # 60 units of Tomato Sauce
    "P010": 70,   # 70 units of Cheese
    "P011": 85,   # 85 units of Cereal
    "P012": 120,  # 120 units of Yogurt
    "P013": 50,   # 50 units of Butter
    "P014": 150,  # 150 units of Bananas
    "P015": 90    # 90 units of Spinach
}
initial_sales = [
    {"product_id": "P001", "quantity": 2, "total_price": 5.98, "date": "2023-11-20"},
    {"product_id": "P004", "quantity": 5, "total_price": 4.95, "date": "2023-11-21"},
    {"product_id": "P007", "quantity": 3, "total_price": 4.50, "date": "2023-11-22"},
    {"product_id": "P010", "quantity": 1, "total_price": 4.50, "date": "2023-11-23"},
    {"product_id": "P012", "quantity": 4, "total_price": 3.20, "date": "2023-11-24"},
    {"product_id": "P015", "quantity": 2, "total_price": 4.00, "date": "2023-11-25"},
    {"product_id": "P008", "quantity": 10, "total_price": 12.00, "date": "2023-11-26"},
    
]
initial_discounts = {
    "P001": 0.10,  # 10% discount on Milk
    "P005": 0.15,  # 15% discount on Chicken
    "P006": 0.05,  # 5% discount on Orange Juice
    "P008": 0.10,  # 10% discount on Pasta
    "P011": 0.20,  # 20% discount on Cereal
    "P014": 0.07,  # 7% discount on Bananas
}

initial_perishable_stock = {
    "P012": {"quantity": 30, "expiry_date": "2023-12-31"},  # Yogurt
    "P010": {"quantity": 20, "expiry_date": "2023-11-15"},  # Cheese
    "P006": {"quantity": 15, "expiry_date": "2023-10-10"},  # Orange Juice
}

for pid, details in initial_products.items():
    product_manager.add_product(pid, details["name"], details["price"])

for pid, quantity in initial_stock.items():
    stock_manager.add_stock(pid, quantity)

for sale in initial_sales:
    sales_manager.record_sale(sale["product_id"], sale["quantity"], sale["total_price"])

for pid, discount_rate in initial_discounts.items():
    discount_manager.add_discount(pid, discount_rate)

for product_id, details in initial_perishable_stock.items():
    perishable_stock_manager.add_perishable_stock(product_id, details["quantity"], details["expiry_date"])

def view_products():
    print("\nProduct List:")
    print("{:<10} {:<20} {:<10}".format('Product ID', 'Name', 'Price'))
    print("-" * 60)
    for pid, details in product_manager.products.items():
        print("{:<10} {:<20} {:<10}".format(pid, details["name"], f'${details["price"]:.2f}'))

def print_menu():
    print("\nSupermarket Management System")
    print("1. Product Management")
    print("2. Stock Management")
    print("3. Sales Management")
    print("4. Discount Management")
    print("5. Manage Perishable Stock")
    print("6. Exit")
    print()

def print_product_menu():
    print("\nProduct Management")
    print("1. View Products")
    print("2. Add Product")
    print("3. Remove Product")
    print("4. Update Product")
    print("5. Return to Main Menu")
    print()

def print_stock_menu():
    print("\n--- Stock Management ---")
    print("1. View Stock")
    print("2. Add Stock")
    print("3. Reduce Stock")
    print("4. Check Perishable Stock (If applicable)")
    print("5. Return to Main Menu")
    print()

def print_sales_menu():
    print("\n--- Sales Management ---")
    print("1. Record a Sale")
    print("2. View Sales Records")
    print("3. View Total Sales")
    print("4. Return to Main Menu")
    print()

def print_discount_menu():
    print("\n--- Discount Management ---")
    print("1. Apply Discount to a Product")
    print("2. Remove Discount from a Product")
    print("3. View Current Discounts")
    print("4. Return to Main Menu")
    print()

def print_perishable_stock_menu():
    print("\n--- Perishable Stock Management ---")
    print("1. Add Perishable Stock")
    print("2. Check for Expired Items")
    print("3. Remove Expired Stock")
    print("4. Return to Stock Management Menu")
    print()

def product_management():
    while True:
        print_product_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            format_product_list(product_manager.products)
        elif choice == "2":
            pid = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            product_manager.add_product(pid, name, price)
            print(f"Product {pid} added.")
        elif choice == "3":
            pid = input("Enter product ID to remove: ")
            product_manager.remove_product(pid)
            print(f"Product {pid} removed.")
        elif choice == "4":
            pid = input("Enter product ID to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            price = input("Enter new price (leave blank to keep current): ")
            price = float(price) if price else None
            product_manager.update_product(pid, name, price)
            print(f"Product {pid} updated.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def stock_management():
    while True:
        print_stock_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            format_stock_list(stock_manager.stock)
        elif choice == "2":
            pid = input("Enter product ID to add stock: ")
            quantity = int(input("Enter quantity: "))
            stock_manager.add_stock(pid, quantity)
            print(f"Stock added for product {pid}.")
        elif choice == "3":
            pid = input("Enter product ID to reduce stock: ")
            quantity = int(input("Enter quantity: "))
            stock_manager.remove_stock(pid, quantity)
            print(f"Stock reduced for product {pid}.")
        elif choice == "4":
            perishable_stock_management()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def sales_management():
    while True:
        print_sales_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            pid = input("Enter product ID for sale: ")
            quantity = int(input("Enter quantity sold: "))
            price = product_manager.products[pid]['price']
            sales_manager.record_sale(pid, quantity, price)
            print(f"Sale recorded for product {pid}.")
        elif choice == "2":
            format_sales_records(sales_manager.sales_records)
        elif choice == "3":
            total_revenue = sales_manager.total_sales()
            print(f"Total Sales Revenue: ${total_revenue:.2f}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def discount_management():
    while True:
        print_discount_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            pid = input("Enter product ID to apply discount: ")
            rate = float(input("Enter discount rate (e.g., 0.1 for 10%): "))
            discount_manager.add_discount(pid, rate)
            print(f"Discount applied to product {pid}.")
        elif choice == "2":
            pid = input("Enter product ID to remove discount: ")
            discount_manager.remove_discount(pid)
            print(f"Discount removed from product {pid}.")
        elif choice == "3":
            format_discount_list(discount_manager.discounts)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def perishable_stock_management():
    while True:
        print_perishable_stock_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            pid = input("Enter perishable product ID to add stock: ")
            quantity = int(input("Enter quantity: "))
            expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
            perishable_stock_manager.add_perishable_stock(pid, quantity, expiry_date)
            print(f"Perishable stock added for product {pid}.")
        elif choice == "2":
            current_date = input("Enter current date (YYYY-MM-DD): ")
            expired_items = perishable_stock_manager.check_expiry(current_date)
            print("Expired Items:", expired_items)
        elif choice == "3":
            current_date = input("Enter current date (YYYY-MM-DD): ")
            perishable_stock_manager.remove_expired_stock(current_date)
            print("Expired items removed.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def format_product_list(products):
    print("\n--- Product List ---")
    for pid, details in products.items():
        print(f"ID: {pid}, Name: {details['name']}, Price: ${details['price']:.2f}")
    if not products:
        print("No products available.")

def format_stock_list(stock):
    print("\n--- Stock Levels ---")
    for pid, quantity in stock.items():
        print(f"Product ID: {pid}, Quantity: {quantity}")
    if not stock:
        print("No stock information available.")

def format_perishable_stock_list(stock):
    print("\n--- Perishable Stock Levels ---")
    for pid, info in stock.items():
        quantity, expiry_date = info['quantity'], info['expiry_date']
        print(f"Product ID: {pid}, Quantity: {quantity}, Expiry Date: {expiry_date}")
    if not stock:
        print("No perishable stock information available.")

def format_sales_records(sales_records):
    print("\n--- Sales Records ---")
    for record in sales_records:
        print(f"Product ID: {record['product_id']}, Quantity: {record['quantity']}, Price: ${record['price']:.2f}")
    if not sales_records:
        print("No sales records available.")

def format_discount_list(discounts):
    print("\n--- Current Discounts ---")
    for pid, discount_rate in discounts.items():
        print(f"Product ID: {pid}, Discount Rate: {discount_rate * 100}%")
    if not discounts:
        print("No discounts available.")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            product_management()
        elif choice == "2":
            stock_management()
        elif choice == "3":
            sales_management()
        elif choice == "4":
            discount_management()
        elif choice == "5":
            perishable_stock_management()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()