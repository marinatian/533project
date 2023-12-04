import unittest
from sales_management.discounts import DiscountManager
from sales_management.sales import SalesManager

class Test_DiscountManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_data = [
            ("P0001", 0.10),
            ("P0002", 0.20),
            ("P0003", 0.05),
        ]
    
    @classmethod
    def tearDownClass(cls):
        del cls.test_data
    
    def setUp(self):
        self.discount_manager = DiscountManager()
        for product_id, discount in self.test_data:
            self.discount_manager.add_discount(product_id, discount)
    
    def tearDown(self):
        self.discount_manager = None
    
    def test_add_discount(self):
        self.discount_manager.add_discount("P0004", 0.15)
        self.assertIn("P0004",self.discount_manager.discounts)
        self.assertEqual(self.discount_manager.discounts["P0004"],0.15)
    
    def test_remove_discount(self):
        self.discount_manager.remove_discount("P0001")
        self.assertNotIn("P0001",self.discount_manager.discounts)
    
    def test_apply_discount_existing(self):
        price = 100
        product_id = "P0002"
        expected_price = price * (1-self.discount_manager.discounts[product_id])
        discounted_price = self.discount_manager.apply_discount(product_id, price)
        self.assertEqual(discounted_price, expected_price)
    
    def test_apply_discount_non_existing(self):
        price = 100
        product_id = "P9999"
        discounted_price = self.discount_manager.apply_discount(product_id,price)
        self.assertEqual(discounted_price, price)

class Test_SalesManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.sales_manager = SalesManager()
    
    def tearDown(self):
        self.sales_manager.sales_records.clear()
    
    def test_record_sale(self):
        self.assertEqual(len(self.sales_manager.sales_records),0)
        self.sales_manager.record_sale("P0001",2,100.0)
        self.assertIn("P0001", self.sales_manager.sales_records[0]['product_id'])
        self.assertEqual(self.sales_manager.sales_records[0]['quantity'],2)
        self.assertEqual(self.sales_manager.sales_records[0]['price'],100.0)
    
    def test_total_sales(self):
        self.sales_manager.record_sale("P0001",2,100.0)
        self.sales_manager.record_sale("P0002",1,200.0)
        self.sales_manager.record_sale("P0003",3,50.0)

        # correct calculation
        excepted_total = (2*100.0) + (1*200.0) + (3*50.0)
        self.assertEqual(self.sales_manager.total_sales(),excepted_total)
        # positive total
        self.assertGreater(self.sales_manager.total_sales(),0)
    
if __name__ == '__main__':
    unittest.main()