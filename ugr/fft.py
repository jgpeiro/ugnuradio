import cmath
from top_block import TopBlock

class FFT(TopBlock):
    def __init__(self, item_size):
        super().__init__()
        self.item_size = item_size
        self.next_block = None

    def set_next(self, block):
        self.next_block = block

    def work(self, input_items, output_items):
        num_samples = len(input_items)
        fft_size = self.get_fft_size(num_samples)
        padded_input = self.pad_input(input_items, fft_size)
        fft_output = self.fft(padded_input)
        output_items.extend(fft_output)

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def get_fft_size(self, num_samples):
        # Find the nearest power of 2 greater than or equal to num_samples
        fft_size = 1
        while fft_size < num_samples:
            fft_size *= 2
        return fft_size

    def pad_input(self, input_items, fft_size):
        # Pad the input with zeros to match the FFT size
        padded_input = input_items + [0] * (fft_size - len(input_items))
        return padded_input

    def fft(self, input_items):
        # Perform the FFT calculation
        num_samples = len(input_items)
        if num_samples <= 1:
            return input_items
        else:
            mid = num_samples // 2
            even = self.fft(input_items[0::2])
            odd = self.fft(input_items[1::2])
            combined = [0] * num_samples
            for i in range(mid):
                twiddle = cmath.exp(-2j * cmath.pi * i / num_samples)
                combined[i] = even[i] + twiddle * odd[i]
                combined[i + mid] = even[i] - twiddle * odd[i]
            return combined

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass