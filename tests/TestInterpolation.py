import unittest
from unittest.mock import MagicMock
from interpolation import Interpolation

class TestInterpolation(unittest.TestCase):
    def setUp(self):
        self.item_size = 1
        self.interp_factor = 3
        self.interpolator = Interpolation(self.item_size, self.interp_factor)

    def test_set_next(self):
        next_block = MagicMock()
        self.interpolator.set_next(next_block)
        self.assertEqual(self.interpolator.next_block, next_block)

    def test_work_with_next_block(self):
        input_items = [1, 2, 3]
        output_items = []
        next_block = MagicMock()
        self.interpolator.set_next(next_block)
        self.interpolator.work(input_items, output_items)
        expected_output_items = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        self.assertEqual(output_items, expected_output_items)
        next_block.work.assert_called_once_with(expected_output_items, None)

    def test_work_without_next_block(self):
        input_items = [1, 2, 3]
        output_items = []
        self.interpolator.work(input_items, output_items)
        expected_output_items = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        self.assertEqual(output_items, expected_output_items)

if __name__ == '__main__':
    unittest.main()