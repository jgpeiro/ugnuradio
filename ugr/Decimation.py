class Decimation(TopBlock):
    def __init__(self, item_size, decim_factor):
        super().__init__()
        self.item_size = item_size
        self.decim_factor = decim_factor
        self.next_block = None

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        num_samples = len(input_items)
        for i in range(0, num_samples, self.decim_factor):
            sample = input_items[i]
            output_items.append(sample)

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass