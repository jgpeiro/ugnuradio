import time
from top_block import TopBlock

class FileSink(TopBlock):
    def __init__(self, item_size, filename):
        super().__init__()
        self.item_size = item_size
        self.filename = filename
        self.file = None
        self.t0 = time.ticks_ms()

    def work(self, input_items, output_items):
        # Write the input items to the file
        if self.file is not None:
            num_samples = len(input_items)
            for i in range(num_samples):
                sample = input_items[i]
                #self.file.write(str(sample) + "\n")
                print( time.ticks_ms() - self.t0, sample )

    def start(self):
        # Open the file for writing
        self.file = open(self.filename, "w")

    def stop(self):
        # Close the file
        if self.file is not None:
            self.file.close()
            self.file = None

    def wait(self):
        pass
