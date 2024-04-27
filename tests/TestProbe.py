import unittest
from unittest.mock import MagicMock
from probe import Probe

class TestProbe(unittest.TestCase):
    def setUp(self):
        self.item_size = 1
        self.callback = MagicMock()
        self.probe = Probe(self.item_size, self.callback)

    def test_set_next(self):
        next_block = MagicMock()
        self.probe.set_next(next_block)
        self.assertEqual(self.probe.next_block, next_block)

    def test_work_with_next_block(self):
        input_items = [1, 2, 3]
        output_items = []
        next_block = MagicMock()
        self.probe.set_next(next_block)
        self.probe.work(input_items, output_items)
        self.assertEqual(output_items, input_items)
        self.callback.assert_has_calls([unittest.mock.call(1), unittest.mock.call(2), unittest.mock.call(3)])
        next_block.work.assert_called_once_with(input_items, None)

    def test_work_without_next_block(self):
        input_items = [1, 2, 3]
        output_items = []
        self.probe.work(input_items, output_items)
        self.assertEqual(output_items, input_items)
        self.callback.assert_has_calls([unittest.mock.call(1), unittest.mock.call(2), unittest.mock.call(3)])

if __name__ == '__main__':
    unittest.main()