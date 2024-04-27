import unittest
from unittest.mock import MagicMock
from fm_modulator import FMModulator

class TestFMModulator(unittest.TestCase):
    def setUp(self):
        self.modulation_index = 0.5
        self.sampling_rate = 1000
        self.modulator = FMModulator(self.modulation_index, self.sampling_rate)

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
        self.assertEqual(len(output_items), len(input_items))
        next_block.work.assert_called_once_with(output_items, None)

    def test_work_without_next_block(self):
        input_items = [1, 2, 3]
        output_items = []
        self.modulator.work(input_items, output_items)
        self.assertEqual(len(output_items), len(input_items))

    def test_start(self):
        self.modulator.start()
        self.assertEqual(self.modulator.phase, 0)

if __name__ == '__main__':
    unittest.main()