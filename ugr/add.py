from top_block import TopBlock

class Add(TopBlock):
    def __init__(self, item_size):
        super().__init__()
        self.item_size = item_size
        self.next_block = None

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        num_inputs = len(input_items)
        num_samples = len(input_items[0])

        for i in range(num_samples):
            sum_value = 0
            for j in range(num_inputs):
                sum_value += input_items[j][i]
            output_items.append(sum_value)

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass