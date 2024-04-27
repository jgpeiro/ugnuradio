import unittest
from unittest.mock import MagicMock
from divide import Divide

class TestDivide(unittest.TestCase):
    def setUp(self):
        self.item_size = 1
        self.factor = 2
        self.divider = Divide(self.item_size, self.factor)

    def test_set_next(self):
        next_block = MagicMock()
        self.divider.set_next(next_block)
        self.assertEqual(self.divider.next_block, next_block)

    def test_work_with_next_block(self):
        input_items = [2, 4, 6]
        output_items = []
        next_block = MagicMock()
        self.divider.set_next(next_block)
        self.divider.work(input_items, output_items)
        expected_output_items = [1, 2, 3]
        self.assertEqual(output_items, expected_output_items)
        next_block.work.assert_called_once_with(expected_output_items, None)

    def test_work_without_next_block(self):
        input_items = [2, 4, 6]
        output_items = []
        self.divider.work(input_items, output_items)
        expected_output_items = [1, 2, 3]
        self.assertEqual(output_items, expected_output_items)

if __name__ == '__main__':
    unittest.main()