import unittest
import main


class TestConvertor(unittest.TestCase):
    def setUp(self):
        self.convertor = main()

    def test_convert(self):
        mass = ['test_1.png', 'test_2.png', 'test_3.png', 'test_4.png']
        self.assertEqual(self.convertor.convert(), mass)


if __name__ == "__main__":
    unittest.main()
