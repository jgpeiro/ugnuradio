import numpy as np

class Interpolation(TopBlock):
    def __init__(self, item_size, interp_factor):
        super().__init__()
        self.item_size = item_size
        self.interp_factor = interp_factor
        self.next_block = None

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        num_samples = len(input_items)
        for i in range(num_samples):
            sample = input_items[i]
            interpolated_samples = np.repeat(sample, self.interp_factor)
            output_items.extend(interpolated_samples)

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass