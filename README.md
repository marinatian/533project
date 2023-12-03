# 533project

Our Supermaket Management System allows users to manage products, stocks, and sales. We will organized our system into two different sections, inventory_management and sales_management. The following are short descriptions of our sub-packages and functions/methods.

Subpackage 1: inventory_management
It will contain two modules ‘stock.py’ and ‘products.py’, for managing the supermarket’s inventory and products.

● Module:stock.py
1st class is for managing general inventory. It will include 2 methods:
1. a method for adding some products to the stock
2. a method for removing some products from the stock
2nd class is for managing perishable goods. It will use inheritance. It will include 1 method:
1. a method for adding some perishable products to stock with an associated expiry date

● Module:products.py
1st class will be responsible for managing the information about products available in the supermarket. It will include 3 methods:
1. a method for adding a new product to the product list
2. a method for removing a product from the product list
3. a method for updating the name and price of an existing product

Subpackage 2: sales_management

● Module:sales.py
It will contain a SalesManager class, offering following functions:
1. record_sale: to record each sale transaction.
2. total_sales method: to calculate the total revenue.

● Module:discounts.py
It will contain a DiscountManager class, offering following functions:
1. add_discount: to apply a new discount to a product.
2. remove_discount: to remove an existing discount from a product when a discount
period ends or if a discount needs to be withdrawn.
3. apply_discount:to calculate the discounted price of a product.
