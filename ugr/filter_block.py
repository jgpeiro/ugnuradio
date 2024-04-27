class InterpolatingFIRFilter(TopBlock):
    def __init__(self, item_size, interpolation, taps, sample_delay):
        super().__init__()
        self.item_size = item_size
        self.interpolation = interpolation
        self.taps = taps
        self.sample_delay = sample_delay
        self.next_block = None
        self.buffer = []

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        num_input_items = len(input_items)
        num_output_items = num_input_items * self.interpolation

        # Append input items to the buffer
        self.buffer.extend(input_items)

        # Perform interpolation and convolution
        for i in range(num_output_items):
            out = 0
            for j in range(len(self.taps)):
                index = i // self.interpolation - j
                if index >= 0 and index < len(self.buffer):
                    out += self.buffer[index] * self.taps[j]
            output_items.append(out)

        # Remove processed items from the buffer
        self.buffer = self.buffer[num_input_items:]

        # Adjust tag locations based on sample delay
        for tag in input_items.tags:
            tag.offset += self.sample_delay

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass