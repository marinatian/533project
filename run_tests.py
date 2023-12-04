
import unittest
from sales_management.test_sales import Test_DiscountManager,Test_SalesManager

def create_suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(Test_DiscountManager))
    suite.addTests(unittest.makeSuite(Test_SalesManager))
    runner = unittest.TextTestRunner(verbosity=2)
    print(runner.run(suite))

create_suite()