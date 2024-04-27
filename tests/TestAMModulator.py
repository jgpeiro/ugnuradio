import unittest
from unittest.mock import MagicMock
from am_modulator import AMModulator

class TestAMModulator(unittest.TestCase):
    def setUp(self):
        self.modulation_index = 0.5
        self.modulator = AMModulator(self.modulation_index)

    def test_set_next(self):
        next_block = MagicMock()
        self.modulator.set_next(next_block)
        self.assertEqual(self.modulator.next_block, next_block)

    def test_work_with_next_block(self):
        input_items = [1, 2, 3]
        output_items = []
        next_block = MagicMock()
        self.modulator.set_next(next_block)
        self.modulator.work(input_items, output_items)
        expected_output_items = [1.5, 4.0, 7.5]
        self.assertEqual(output_items, expected_output_items)
        next_block.work.assert_called_once_with(expected_output_items, None)

    def test_work_without_next_block(self):
        input_items = [1, 2, 3]
        output_items = []
        self.modulator.work(input_items, output_items)
        expected_output_items = [1.5, 4.0, 7.5]
        self.assertEqual(output_items, expected_output_items)

if __name__ == '__main__':
    unittest.main()