from top_block import TopBlock

class _Throttle(TopBlock):
    def __init__(self, item_size, sample_rate):
        super().__init__()
        self.item_size = item_size
        self.sample_rate = sample_rate
        self.next_block = None

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        # Throttle the input items based on the sample rate
        # Implement the throttling logic here
        # ...
        output_items = input_items
        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass

import time

class Throttle(TopBlock):
    def __init__(self, item_size, sample_rate):
        super().__init__()
        self.item_size = item_size
        self.sample_rate = sample_rate
        self.next_block = None
        self.last_work_time = time.time()
        self.acc_data_len = 0

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        # Calculate the expected time interval based on the sample rate
        expected_interval = 1.0 / self.sample_rate

        # Calculate the actual time interval since the last work call
        current_time = time.time()
        actual_interval = current_time - self.last_work_time
        self.last_work_time = current_time

        # Calculate the accumulated data length
        data_len = len(input_items)
        self.acc_data_len += data_len

        # Calculate the expected time based on the accumulated data length
        expected_time = self.acc_data_len * self.item_size / self.sample_rate

        # Calculate the time difference between the expected and actual time
        time_diff = expected_time - actual_interval

        # If the time difference is greater than zero, sleep for the remaining time
        if time_diff > 0:
            sleep_time_us = int(time_diff * 1000000)
            time.sleep_us(sleep_time_us)

        # Pass the input items to the output items
        output_items[:] = input_items

        # Reset the accumulated data length
        self.acc_data_len = 0

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        self.last_work_time = time.time()
        self.acc_data_len = 0

    def stop(self):
        pass

    def wait(self):
        pass