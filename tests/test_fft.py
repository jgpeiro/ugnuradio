import unittest
from unittest.mock import MagicMock
from fft import FFT

class TestFFT(unittest.TestCase):
    def setUp(self):
        self.item_size = 1
        self.fft_block = FFT(self.item_size)

    def test_set_next(self):
        next_block = MagicMock()
        self.fft_block.set_next(next_block)
        self.assertEqual(self.fft_block.next_block, next_block)

    def test_work_with_next_block(self):
        input_items = [1, 2, 3, 4]
        output_items = []
        next_block = MagicMock()
        self.fft_block.set_next(next_block)
        self.fft_block.work(input_items, output_items)
        self.assertEqual(len(output_items), 4)
        next_block.work.assert_called_once_with(output_items, None)

    def test_work_without_next_block(self):
        input_items = [1, 2, 3, 4]
        output_items = []
        self.fft_block.work(input_items, output_items)
        self.assertEqual(len(output_items), 4)

    def test_fft(self):
        input_items = [1, 2, 3, 4]
        expected_output = [10, -2+2j, -2, -2-2j]
        output = self.fft_block.fft(input_items)
        self.assertEqual(len(output), len(expected_output))
        for i in range(len(output)):
            self.assertAlmostEqual(output[i].real, expected_output[i].real, places=3)
            self.assertAlmostEqual(output[i].imag, expected_output[i].imag, places=3)

if __name__ == '__main__':
    unittest.main()