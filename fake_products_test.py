import unittest

import fake_products


class ProductsTest(unittest.TestCase):

    @classmethod
    def setUpClass(ProductsTest):
        ProductsTest.ins = fake_products.Product()

    def test_is_this_thing_on(self):
        self.assertEqual('BUTTS', ProductsTest.ins.part_number())


if __name__ == '__main__':
    unittest.main()
