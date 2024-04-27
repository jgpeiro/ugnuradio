class AMModulator(TopBlock):
    def __init__(self, modulation_index):
        super().__init__()
        self.modulation_index = modulation_index
        self.next_block = None

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        num_samples = len(input_items)
        for i in range(num_samples):
            sample = input_items[i]
            modulated_sample = (1 + self.modulation_index * sample) * sample
            output_items.append(modulated_sample)

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass