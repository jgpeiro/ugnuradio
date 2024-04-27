import math
import numpy as np

class ConstellationModulator(TopBlock):
    def __init__(self, constellation, samples_per_symbol, differential, excess_bw, verbose, log):
        super().__init__()
        self.constellation = constellation
        self.samples_per_symbol = samples_per_symbol
        self.differential = differential
        self.excess_bw = excess_bw
        self.verbose = verbose
        self.log = log
        self.next_block = None
        self.rrc_taps = self.rrc_filter_taps()

    def set_next(self, block):
        self.next_block = block

    def rrc_filter_taps(self):
        # Generate RRC filter taps based on excess bandwidth
        num_taps = 11 * self.samples_per_symbol
        t = np.arange(-num_taps // 2, num_taps // 2 + 1)
        h = np.sinc(t / self.samples_per_symbol) * np.cos(math.pi * self.excess_bw * t / self.samples_per_symbol) / (1 - (2 * self.excess_bw * t / self.samples_per_symbol) ** 2)
        h /= np.sqrt(np.sum(h ** 2))
        return h

    def work(self, input_items, output_items):
        num_symbols = len(input_items)
        for i in range(num_symbols):
            symbol = input_items[i]
            if self.differential:
                symbol = (symbol + self.constellation.points[i % len(self.constellation.points)]) % len(self.constellation.points)
            modulated_symbol = self.constellation.points[symbol]
            upsampled_symbol = np.zeros(self.samples_per_symbol, dtype=np.complex64)
            upsampled_symbol[0] = modulated_symbol
            filtered_symbol = np.convolve(upsampled_symbol, self.rrc_taps, mode='same')
            output_items.extend(filtered_symbol)

        if self.verbose:
            print(f"Modulated {num_symbols} symbols")

        if self.log:
            # Log modulation data to files
            pass

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass