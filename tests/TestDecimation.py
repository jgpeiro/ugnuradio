import unittest
from unittest.mock import MagicMock
from decimation import Decimation

class TestDecimation(unittest.TestCase):
    def setUp(self):
        self.item_size = 1
        self.decim_factor = 3
        self.decimator = Decimation(self.item_size, self.decim_factor)

    def test_set_next(self):
        next_block = MagicMock()
        self.decimator.set_next(next_block)
        self.assertEqual(self.decimator.next_block, next_block)

    def test_work_with_next_block(self):
        input_items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        output_items = []
        next_block = MagicMock()
        self.decimator.set_next(next_block)
        self.decimator.work(input_items, output_items)
        expected_output_items = [1, 4, 7]
        self.assertEqual(output_items, expected_output_items)
        next_block.work.assert_called_once_with(expected_output_items, None)

    def test_work_without_next_block(self):
        input_items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        output_items = []
        self.decimator.work(input_items, output_items)
        expected_output_items = [1, 4, 7]
        self.assertEqual(output_items, expected_output_items)

if __name__ == '__main__':
    unittest.main()