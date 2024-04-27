import unittest
from unittest.mock import MagicMock
from add import Add

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.item_size = 1
        self.add_block = Add(self.item_size)

    def test_set_next(self):
        next_block = MagicMock()
        self.add_block.set_next(next_block)
        self.assertEqual(self.add_block.next_block, next_block)

    def test_work_with_next_block(self):
        input_items = [[1, 2, 3], [4, 5, 6]]
        output_items = []
        next_block = MagicMock()
        self.add_block.set_next(next_block)
        self.add_block.work(input_items, output_items)
        self.assertEqual(output_items, [5, 7, 9])
        next_block.work.assert_called_once_with([5, 7, 9], None)

    def test_work_without_next_block(self):
        input_items = [[1, 2, 3], [4, 5, 6]]
        output_items = []
        self.add_block.work(input_items, output_items)
        self.assertEqual(output_items, [5, 7, 9])

    def test_work_with_different_input_sizes(self):
        input_items = [[1, 2, 3], [4, 5]]
        output_items = []
        self.add_block.work(input_items, output_items)
        self.assertEqual(output_items, [5, 7])

if __name__ == '__main__':
    unittest.main()