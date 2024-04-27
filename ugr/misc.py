Certainly! Here's the implementation of the Time Delay, Threshold, Selector, and GUI Widgets blocks along with their unit tests:

Time Delay Block:
```python
class TimeDelay(TopBlock):
    def __init__(self, item_size, delay):
        super().__init__()
        self.item_size = item_size
        self.delay = delay
        self.next_block = None
        self.buffer = []

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        num_samples = len(input_items)
        for i in range(num_samples):
            sample = input_items[i]
            self.buffer.append(sample)
            if len(self.buffer) > self.delay:
                delayed_sample = self.buffer.pop(0)
                output_items.append(delayed_sample)

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        self.buffer = []

    def stop(self):
        pass

    def wait(self):
        pass
```

Time Delay Unit Tests:
```python
import unittest
from unittest.mock import MagicMock
from time_delay import TimeDelay

class TestTimeDelay(unittest.TestCase):
    def setUp(self):
        self.item_size = 1
        self.delay = 2
        self.time_delay = TimeDelay(self.item_size, self.delay)

    def test_set_next(self):
        next_block = MagicMock()
        self.time_delay.set_next(next_block)
        self.assertEqual(self.time_delay.next_block, next_block)

    def test_work_with_next_block(self):
        input_items = [1, 2, 3, 4, 5]
        output_items = []
        next_block = MagicMock()
        self.time_delay.set_next(next_block)
        self.time_delay.work(input_items, output_items)
        self.assertEqual(output_items, [1, 2, 3])
        next_block.work.assert_called_once_with([1, 2, 3], None)

    def test_work_without_next_block(self):
        input_items = [1, 2, 3, 4, 5]
        output_items = []
        self.time_delay.work(input_items, output_items)
        self.assertEqual(output_items, [1, 2, 3])

    def test_start(self):
        self.time_delay.start()
        self.assertEqual(self.time_delay.buffer, [])

if __name__ == '__main__':
    unittest.main()
```

Threshold Block:
```python
class Threshold(TopBlock):
    def __init__(self, item_size, threshold):
        super().__init__()
        self.item_size = item_size
        self.threshold = threshold
        self.next_block = None

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        num_samples = len(input_items)
        for i in range(num_samples):
            sample = input_items[i]
            if sample >= self.threshold:
                output_items.append(1)
            else:
                output_items.append(0)

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass
```

Threshold Unit Tests:
```python
import unittest
from unittest.mock import MagicMock
from threshold import Threshold

class TestThreshold(unittest.TestCase):
    def setUp(self):
        self.item_size = 1
        self.threshold = 3
        self.threshold_block = Threshold(self.item_size, self.threshold)

    def test_set_next(self):
        next_block = MagicMock()
        self.threshold_block.set_next(next_block)
        self.assertEqual(self.threshold_block.next_block, next_block)

    def test_work_with_next_block(self):
        input_items = [1, 2, 3, 4, 5]
        output_items = []
        next_block = MagicMock()
        self.threshold_block.set_next(next_block)
        self.threshold_block.work(input_items, output_items)
        self.assertEqual(output_items, [0, 0, 1, 1, 1])
        next_block.work.assert_called_once_with([0, 0, 1, 1, 1], None)

    def test_work_without_next_block(self):
        input_items = [1, 2, 3, 4, 5]
        output_items = []
        self.threshold_block.work(input_items, output_items)
        self.assertEqual(output_items, [0, 0, 1, 1, 1])

if __name__ == '__main__':
    unittest.main()
```

Selector Block:
```python
class Selector(TopBlock):
    def __init__(self, item_size, num_inputs, selected_input):
        super().__init__()
        self.item_size = item_size
        self.num_inputs = num_inputs
        self.selected_input = selected_input
        self.next_block = None

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        selected_items = input_items[self.selected_input]
        output_items.extend(selected_items)

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass
```

Selector Unit Tests:
```python
import unittest
from unittest.mock import MagicMock
from selector import Selector

class TestSelector(unittest.TestCase):
    def setUp(self):
        self.item_size = 1
        self.num_inputs = 3
        self.selected_input = 1
        self.selector = Selector(self.item_size, self.num_inputs, self.selected_input)

    def test_set_next(self):
        next_block = MagicMock()
        self.selector.set_next(next_block)
        self.assertEqual(self.selector.next_block, next_block)

    def test_work_with_next_block(self):
        input_items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        output_items = []
        next_block = MagicMock()
        self.selector.set_next(next_block)
        self.selector.work(input_items, output_items)
        self.assertEqual(output_items, [4, 5, 6])
        next_block.work.assert_called_once_with([4, 5, 6], None)

    def test_work_without_next_block(self):
        input_items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        output_items = []
        self.selector.work(input_items, output_items)
        self.assertEqual(output_items, [4, 5, 6])

if __name__ == '__main__':
    unittest.main()
```

GUI Widgets Block:
```python
class GUIWidgets(TopBlock):
    def __init__(self, item_size, widget_type, callback):
        super().__init__()
        self.item_size = item_size
        self.widget_type = widget_type
        self.callback = callback
        self.next_block = None

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        # Assuming the GUI widget updates the input items based on user interaction
        output_items.extend(input_items)

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        # Create and display the GUI widget based on the widget_type
        pass

    def stop(self):
        # Close and cleanup the GUI widget
        pass

    def wait(self):
        # Wait for the GUI widget to be closed
        pass
```

GUI Widgets Unit Tests:
```python
import unittest
from unittest.mock import MagicMock
from gui_widgets import GUIWidgets

class TestGUIWidgets(unittest.TestCase):
    def setUp(self):
        self.item_size = 1
        self.widget_type = "slider"
        self.callback = MagicMock()
        self.gui_widgets = GUIWidgets(self.item_size, self.widget_type, self.callback)

    def test_set_next(self):
        next_block = MagicMock()
        self.gui_widgets.set_next(next_block)
        self.assertEqual(self.gui_widgets.next_block, next_block)

    def test_work_with_next_block(self):
        input_items = [1, 2, 3]
        output_items = []
        next_block = MagicMock()
        self.gui_widgets.set_next(next_block)
        self.gui_widgets.work(input_items, output_items)
        self.assertEqual(output_items, [1, 2, 3])
        next_block.work.assert_called_once_with([1, 2, 3], None)

    def test_work_without_next_block(self):
        input_items = [1, 2, 3]
        output_items = []
        self.gui_widgets.work(input_items, output_items)
        self.assertEqual(output_items, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
```

Explanation:
- The `TimeDelay` block introduces a delay in the signal by buffering the input samples and outputting them after a specified delay. It maintains a buffer to store the delayed samples.
- The `Threshold` block converts analog signals into digital by applying a threshold. It compares each input sample with the threshold and outputs 1 if the sample is greater than or equal to the threshold, and 0 otherwise.
- The `Selector` block selects a subset of streams from multiple inputs. It takes the number of input streams and the index of the selected input stream as parameters. It passes the selected input stream to the output.
- The `GUIWidgets` block represents a generic GUI widget block. It assumes that the GUI widget updates the input items based on user interaction. The specific implementation of the GUI widget is not provided in this example.
- The unit tests for each block follow a similar structure to the previous examples, testing the `set_next` method and the `work` method with and without a next block. The tests for the `GUIWidgets` block are simplified since the actual GUI widget implementation is not included.

These blocks provide additional functionality for signal processing and user interaction in your flowgraph. The time delay block introduces a delay in the signal, the threshold block converts analog signals to digital, the selector block selects a subset of input streams, and the GUI widgets block allows for interactive control and visualization of the signal.

Remember to adapt the GUI widgets block implementation based on the specific GUI framework you are using (e.g., WX, Qt) and the desired widget types and behaviors.