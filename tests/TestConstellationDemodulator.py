import unittest
from unittest.mock import MagicMock
from constellation_demodulator import ConstellationDemodulator

class TestConstellationDemodulator(unittest.TestCase):
    def setUp(self):
        self.constellation = MagicMock()
        self.constellation.points = [1 + 1j, -1 + 1j, -1 - 1j, 1 - 1j]
        self.constellation.decision.side_effect = lambda x: np.argmin(np.abs(x - self.constellation.points))
        self.samples_per_symbol = 4
        self.differential = True
        self.excess_bw = 0.35
        self.verbose = True
        self.log = False
        self.demodulator = ConstellationDemodulator(self.constellation, self.samples_per_symbol, self.differential, self.excess_bw, self.verbose, self.log)

    def test_set_next(self):
        next_block = MagicMock()
        self.demodulator.set_next(next_block)
        self.assertEqual(self.demodulator.next_block, next_block)

    def test_work_with_next_block(self):
        input_items = [1 + 1j, 1 + 1j, 1 + 1j, 1 + 1j, -1 + 1j, -1 + 1j, -1 + 1j, -1 + 1j]
        output_items = []
        next_block = MagicMock()
        self.demodulator.set_next(next_block)
        self.demodulator.work(input_items, output_items)
        self.assertEqual(len(output_items), len(input_items) // self.samples_per_symbol)
        next_block.work.assert_called_once_with(output_items, None)

    def test_work_without_next_block(self):
        input_items = [1 + 1j, 1 + 1j, 1 + 1j, 1 + 1j, -1 + 1j, -1 + 1j, -1 + 1j, -1 + 1j]
        output_items = []
        self.demodulator.work(input_items, output_items)
        self.assertEqual(len(output_items), len(input_items) // self.samples_per_symbol)

if __name__ == '__main__':
    unittest.main()