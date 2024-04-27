import unittest
from unittest.mock import MagicMock
from kalman_filter import KalmanFilter

class TestKalmanFilter(unittest.TestCase):
    def setUp(self):
        self.item_size = 1
        self.process_noise = 0.1
        self.measurement_noise = 0.1
        self.initial_estimate = 0.0
        self.kalman_filter = KalmanFilter(self.item_size, self.process_noise, self.measurement_noise, self.initial_estimate)

    def test_set_next(self):
        next_block = MagicMock()
        self.kalman_filter.set_next(next_block)
        self.assertEqual(self.kalman_filter.next_block, next_block)

    def test_work_with_next_block(self):
        input_items = [1.0, 2.0, 3.0, 4.0, 5.0]
        output_items = []
        next_block = MagicMock()
        self.kalman_filter.set_next(next_block)
        self.kalman_filter.work(input_items, output_items)
        self.assertEqual(len(output_items), len(input_items))
        next_block.work.assert_called_once_with(output_items, None)

    def test_work_without_next_block(self):
        input_items = [1.0, 2.0, 3.0, 4.0, 5.0]
        output_items = []
        self.kalman_filter.work(input_items, output_items)
        self.assertEqual(len(output_items), len(input_items))

if __name__ == '__main__':
    unittest.main()