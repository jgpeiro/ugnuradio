import numpy as np

class ConstellationDemodulator(TopBlock):
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
        num_samples = len(input_items)
        num_symbols = num_samples // self.samples_per_symbol
        for i in range(num_symbols):
            start = i * self.samples_per_symbol
            end = start + self.samples_per_symbol
            filtered_samples = np.convolve(input_items[start:end], self.rrc_taps, mode='same')
            demodulated_symbol = self.constellation.decision(filtered_samples[-1])
            if self.differential:
                demodulated_symbol = (demodulated_symbol - self.constellation.points[i % len(self.constellation.points)]) % len(self.constellation.points)
            output_items.append(demodulated_symbol)

        if self.verbose:
            print(f"Demodulated {num_symbols} symbols")

        if self.log:
            # Log demodulation data to files
            pass

        if self.next_block is not None:
            self.next_block.work(output_items, None)

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass