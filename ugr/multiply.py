from top_block import TopBlock

class Multiply(TopBlock):
    def __init__(self, item_size, factor):
        super().__init__()
        self.item_size = item_size
        self.factor = factor
        self.next_block = None

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        num_samples = len(input_items)
        for i in range(num_samples):
            sample = input_items[i]
            multiplied_sample = sample * self.factor
            output_items.append(multiplied_sample)

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass