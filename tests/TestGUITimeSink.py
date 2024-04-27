import unittest
from unittest.mock import MagicMock, patch
from gui_time_sink import GUITimeSink

class TestGUITimeSink(unittest.TestCase):
    def setUp(self):
        self.item_size = 1
        self.width = 128
        self.height = 64
        self.gui_time_sink = GUITimeSink(self.item_size, self.width, self.height)

    def test_set_next(self):
        next_block = MagicMock()
        self.gui_time_sink.set_next(next_block)
        self.assertEqual(self.gui_time_sink.next_block, next_block)

    def test_work_with_next_block(self):
        input_items = [1, 2, 3, 4]
        next_block = MagicMock()
        self.gui_time_sink.set_next(next_block)
        self.gui_time_sink.work(input_items, None)
        self.assertEqual(self.gui_time_sink.data, input_items)
        next_block.work.assert_called_once_with(input_items, None)

    def test_work_without_next_block(self):
        input_items = [1, 2, 3, 4]
        self.gui_time_sink.work(input_items, None)
        self.assertEqual(self.gui_time_sink.data, input_items)

    @patch.object(GUITimeSink, 'update_screen')
    def test_update_plot(self, mock_update_screen):
        self.gui_time_sink.data = [1, 2, 3, 4]
        self.gui_time_sink.update_plot()
        mock_update_screen.assert_called_once()

    @patch.object(GUITimeSink, 'update_screen')
    def test_draw_grid(self, mock_update_screen):
        self.gui_time_sink.draw_grid()
        # Assert that the grid lines are drawn correctly
        # You can check the framebuffer contents or use mocks to verify the expected behavior

if __name__ == '__main__':
    unittest.main()