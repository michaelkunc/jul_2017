import unittest

import fake_products


class ProductsTest(unittest.TestCase):

    @classmethod
    def setUpClass(ProductsTest):
        ProductsTest.ins = fake_products.Product()

    def test_part_number(self):
        number_re = r'^[A-Z]{3}-[0-9]{8}$'
        self.assertRegex(ProductsTest.ins.part_number(), number_re)

    def test_part_name(self):
        self.assertEqual('Beatrix Lestrange', ProductsTest.ins.name())


if __name__ == '__main__':
    unittest.main()
