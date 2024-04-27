import unittest
from unittest.mock import MagicMock, patch
from device_source import DeviceSource
from device_sink import DeviceSink

class TestDeviceSource(unittest.TestCase):
    def setUp(self):
        self.item_size = 10
        self.device_type = "SPI"
        self.device_config = {"baudrate": 1000000, "polarity": 0, "phase": 0, "bits": 8, "firstbit": 0}
        self.device_source = DeviceSource(self.item_size, self.device_type, self.device_config)

    def test_set_next(self):
        next_block = MagicMock()
        self.device_source.set_next(next_block)
        self.assertEqual(self.device_source.next_block, next_block)

    @patch("machine.SPI")
    def test_work_with_next_block(self, mock_spi):
        mock_spi.return_value.read.return_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        output_items = []
        next_block = MagicMock()
        self.device_source.set_next(next_block)
        self.device_source.device = mock_spi.return_value
        self.device_source.work([], output_items)
        self.assertEqual(output_items, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        next_block.work.assert_called_once_with([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], None)

    @patch("machine.SPI")
    def test_work_without_next_block(self, mock_spi):
        mock_spi.return_value.read.return_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        output_items = []
        self.device_source.device = mock_spi.return_value
        self.device_source.work([], output_items)
        self.assertEqual(output_items, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    @patch("machine.SPI")
    def test_start(self, mock_spi):
        self.device_source.start()
        mock_spi.assert_called_once_with(**self.device_config)
        self.assertIsNotNone(self.device_source.device)

    def test_stop(self):
        self.device_source.device = MagicMock()
        self.device_source.stop()
        self.device_source.device.deinit.assert_called_once()
        self.assertIsNone(self.device_source.device)


class TestDeviceSink(unittest.TestCase):
    def setUp(self):
        self.item_size = 10
        self.device_type = "SPI"
        self.device_config = {"baudrate": 1000000, "polarity": 0, "phase": 0, "bits": 8, "firstbit": 0}
        self.device_sink = DeviceSink(self.item_size, self.device_type, self.device_config)

    def test_set_next(self):
        next_block = MagicMock()
        self.device_sink.set_next(next_block)
        self.assertEqual(self.device_sink.next_block, next_block)

    @patch("machine.SPI")
    def test_work_with_next_block(self, mock_spi):
        input_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        next_block = MagicMock()
        self.device_sink.set_next(next_block)
        self.device_sink.device = mock_spi.return_value
        self.device_sink.work(input_items, [])
        mock_spi.return_value.write.assert_called_once_with(input_items)
        next_block.work.assert_called_once_with(input_items, None)

    @patch("machine.SPI")
    def test_work_without_next_block(self, mock_spi):
        input_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.device_sink.device = mock_spi.return_value
        self.device_sink.work(input_items, [])
        mock_spi.return_value.write.assert_called_once_with(input_items)

    @patch("machine.SPI")
    def test_start(self, mock_spi):
        self.device_sink.start()
        mock_spi.assert_called_once_with(**self.device_config)
        self.assertIsNotNone(self.device_sink.device)

    def test_stop(self):
        self.device_sink.device = MagicMock()
        self.device_sink.stop()
        self.device_sink.device.deinit.assert_called_once()
        self.assertIsNone(self.device_sink.device)


if __name__ == "__main__":
    unittest.main()