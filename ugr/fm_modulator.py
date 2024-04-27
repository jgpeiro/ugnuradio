import math

class FMModulator(TopBlock):
    def __init__(self, modulation_index, sampling_rate):
        super().__init__()
        self.modulation_index = modulation_index
        self.sampling_rate = sampling_rate
        self.next_block = None
        self.phase = 0

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        num_samples = len(input_items)
        for i in range(num_samples):
            sample = input_items[i]
            phase_deviation = 2 * math.pi * self.modulation_index * sample / self.sampling_rate
            modulated_sample = math.cos(self.phase)
            self.phase += phase_deviation
            output_items.append(modulated_sample)

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        self.phase = 0

    def stop(self):
        pass

    def wait(self):
        pass